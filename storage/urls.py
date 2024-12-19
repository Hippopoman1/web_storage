
from django.urls import path
from .views import *
urlpatterns = [
   path('register/', register_view, name='register'),
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
]