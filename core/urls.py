from django.urls import path
from . import views

urlpatterns = [
    # Коли користувач заходить на головну сторінку '', викликається функція home_page
    path('', views.home_page, name='home'),
]