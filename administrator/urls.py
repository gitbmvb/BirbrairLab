from django.urls import path
from . import views

app_name = "administrator"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
#    path("meet", views.MeetView.as_view(), name="meet"),
#    path("research", views.ResearchView.as_view(), name="research"),
#    path("team", views.TeamView.as_view(), name="team"),
#    path("publications", views.PublicationsView.as_view(), name="publications"),
    path("news", views.NewsView.as_view(), name="news"),
    path("news/add", views.AddNews.as_view(), name="addNews"),
#    path("opportunities", views.OpportunitiesView.as_view(), name="opportunities"),
#    path("donate", views.DonateView.as_view(), name="donate"),
#    path("directions", views.DirectionsView.as_view(), name="directions"),
]