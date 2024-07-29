import os

from django.shortcuts import render
from django.views import View
from mebelevv.models import *
from django.core.files.storage import FileSystemStorage
import requests
from dotenv import load_dotenv

load_dotenv()


def telegramSendMessage(phoneNumber, answers, file):
    message = f"Номер телефона: {phoneNumber}\n\n"
    if file:
        message += f"Прикреплённые файлы: https://mebelevv.kz/files/form_images/{file}\n\n"
    for index, (key, value) in enumerate(zip(answers.keys(), answers.values())):
        message += f"{index + 1}. <b>{key}</b> — {value}\n"

    botToken = os.getenv('TG_BOT_TOKEN')
    botChatID = os.getenv('TG_CHAT_ID')
    sendText = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatID + '&parse_mode=html&text=' + message
    response = requests.get(sendText)
    return response.json()


class MainPage(View):

    def get(self, request):
        questions = Question.objects.all()
        gallery = Gallery.objects.all()
        return render(request, 'mebelevv/index.html', context={'gallery': gallery, 'questions': questions})

    def post(self, request):
        answers = {}
        for q in Question.objects.all():
            answers[request.POST.get(q.title).split(' // ')[0]] = request.POST.get(q.title).split(' // ')[1]
        phoneNumber = request.POST.get('phoneNumber')
        filename = None
        if request.method == 'POST' and request.FILES:
            file = request.FILES['userFile']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
        UserInfo(answers=answers, phoneNumber=phoneNumber, img=filename).save()

        questions = Question.objects.all()
        gallery = Gallery.objects.all()
        telegramSendMessage(phoneNumber, answers, filename)
        return render(request, 'mebelevv/index.html', context={'gallery': gallery, 'questions': questions})
