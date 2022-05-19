from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "main/index.html"


class MeetView(TemplateView):
    template_name = "main/meet.html"


class ResearchView(TemplateView):
    template_name = "main/research.html"


class TeamView(TemplateView):
    template_name = "main/team.html"


class PublicationsView(TemplateView):
    template_name = "main/publications.html"


class NewsView(TemplateView):
    template_name = "main/news.html"


class OpportunitiesView(TemplateView):
    template_name = "main/opportunities.html"


class DonateView(TemplateView):
    template_name = "main/donate.html"


class DirectionsView(TemplateView):
    template_name = "main/directions.html"

