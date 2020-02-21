from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('home/add_post/', views.add_post, name='add'),
    path('home/vote/<int:id_post>', views.vote, name='vote')
]
