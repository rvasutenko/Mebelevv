from django.contrib import admin
from mebelevv.models import *

from django.contrib import admin


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
    list_filter = ('title', 'date',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('answers',)
    list_filter = ('title', 'answers',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('title', 'img',)
    list_filter = ('title', 'img',)
    readonly_fields = ['image_tag']


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    fields = ('phoneNumber', 'answers', 'img', 'image_tag')
    readonly_fields = ('answers', 'image_tag', 'phoneNumber', 'img')
    list_display = ('phoneNumber', 'answers', 'img')
    list_filter = ('answers', 'phoneNumber')
