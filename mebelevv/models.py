from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.postgres.fields import ArrayField


class Gallery(models.Model):
    title = models.CharField('Заголовок', max_length=30)
    date = models.DateField('Дата', auto_now=True)
    img = models.ImageField('Фото', upload_to='gallery', null=True, blank=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Галерея"
        verbose_name = "экземпляр"


class Question(models.Model):
    order = models.PositiveSmallIntegerField('Порядок вопроса', blank=False, null=False, default=1)
    title = models.CharField('Заголовок', max_length=30)
    answers = models.ManyToManyField('Answer', verbose_name='Ответы', max_length=1000, blank=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Вопросы"
        verbose_name = "Вопрос"


class Answer(models.Model):
    title = models.CharField('Заголовок', max_length=30)
    img = models.ImageField('Фото', upload_to='form_images', null=True, blank=True)

    def image_tag(self):
        return mark_safe('<img src="%s" style="max-width: 400px;" />' % self.img.url)
    image_tag.short_description = 'Image'

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Ответы"
        verbose_name = "Ответ"


class UserInfo(models.Model):
    answers = models.JSONField('Ответы')
    phoneNumber = models.CharField('Номер телефона', max_length=16)
    img = models.ImageField('Фото', upload_to='users_images', null=True, blank=True)

    def image_tag(self):
        return mark_safe('<img src="%s" style="max-width: 400px;" />' % self.img.url)
    image_tag.short_description = 'Image'

    def __str__(self):
        return f"{self.phoneNumber}"

    class Meta:
        verbose_name_plural = "Ответы пользователей"
        verbose_name = "Ответ пользователя"