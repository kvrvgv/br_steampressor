

from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id_>', views.post, name='post'),
    path('about', views.about, name='about'),
    path('video', views.video, name='video'),
    path('contacts', views.contacts, name='contacts'),
    path('profile', views.profile, name='profile'),
    path('poll', views.poll, name='poll'),

    path('auth/signup', views.signup, name='signup'),
    path('auth/login', views.login_, name='login'),
    path('auth/logout', views.logout_, name='logout'),
]
