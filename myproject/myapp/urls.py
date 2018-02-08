from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # For registration
    url(r'^register/', views.register, name='register'),
    # For login
    url(r'^login/', views.login , name = 'login'),
    # For home
    url(r'^home' , views.home , name = 'home'),
    # For Creating Quizzes
    url(r'^quiz' , views.quiz , name = 'quiz'),
    # For playing Quizzes
    url(r'^play' , views.play , name = 'play'),
    # for displaying score after the quiz
    url(r'^myscore' , views.myscore, name = 'myscore'),
    # For Leaderboards
    url(r'^leaderboard' , views.leaderboard, name = 'leaderboard')
]