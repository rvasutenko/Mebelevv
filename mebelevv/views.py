from django.shortcuts import render
from django.views import View
from mebelevv.models import *
from django.core.files.storage import FileSystemStorage


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
        return render(request, 'mebelevv/index.html', context={'gallery': gallery, 'questions': questions})
