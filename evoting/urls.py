
from . import views
from django.urls import path,include

urlpatterns = [
    path("",views.index , name="index"),
    path("about.html",views.about , name="about.html"),
    path("registration.html",views.registration , name = "registration.html"),
    path("login.html",views.login , name="login.html"),
    path("contect.html",views.contect , name="contect.html"),
    path("result.html",views.result , name="result.html"),
    path("index.html",views.index , name="index.html"),
    path("logout.html",views.logout , name="logout.html"),
    path("party.html",views.party1 , name="party.html"),
    path("vote.html",views.vote , name="vote.html"),
    path("profile.html",views.profile , name="profile.html"),
    path("edit_profile.html",views.edit_profile , name="edit_profile.html"),
    path("update_vote",views.update_vote ),
    path("feedback.html",views.feedback,name="feedback.html")
    
]