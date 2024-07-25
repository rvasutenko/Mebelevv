from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from mebelevv.models import Gallery


# Create your views here.


class StartingPageView(View):
    template_name = 'mebelevv/index1.html'

    def get(self, request):
        return render(request, self.template_name)


class GalleryPageView(ListView):
    template_name = 'mebelevv/gallery.html'
    model = Gallery
    ordering = ['-date']
    context_object_name = 'gallery'
