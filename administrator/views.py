from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "administrator/index.html"


class NewsView(TemplateView):
    template_name = "administrator/news.html"


class AddNews(TemplateView):
    template_name = "administrator/add_news.html"
