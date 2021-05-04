from django.urls import path
from .views import save_song, get_songs, song_info, home

urlpatterns = [
    path('', home),
    path('save/', save_song),
    path('info/', get_songs),
    path('info/<int:song_id>', song_info),
]

