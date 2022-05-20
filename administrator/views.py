from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


#def index(request):
#    return render(request, "administrator/index.html", {})

class NewsView(TemplateView):
    template_name = "administrator/news.html"
