from django.urls import path
from .views import main


urlpatterns = [
    path('', main, name='index'),
    path('detail/<int:chat_id>/', main, name='main'),
]