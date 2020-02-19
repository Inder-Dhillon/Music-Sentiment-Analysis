from django.urls import path
from . import views

urlpatterns = [
    path('create_title', views.create_title, name='create_title'),
    path('get_songs_to_fill_lyrics', views.get_songs_to_fill_lyrics, name='get_songs_to_fill_lyrics'),
    path('add_lyrics', views.add_lyrics, name='add_lyrics'),
    # path('get_song_for_sentiment', views.get_song_for_sentiment, name='get_song_for_sentiment'),
    
    
]