from django.shortcuts import render
from .models import Song 
from django.http import HttpResponse,JsonResponse
from django.core import serializers

# Create your views here.
def create_title(request):   
        title = request.GET.get("title")
        artist = request.GET.get("title")
        lyric = request.GET.get("lyric")
        if title and artist and lyric:
            Song.objects.update_or_create(title=title,defaults={"artist":artist,"lyric":lyric})
            return HttpResponse(f"Title: {title} created.")
        else:
            return HttpResponse(f"Title is empty!")
        
        
def get_songs_to_fill_lyrics(request):
    songs = Song.objects.all()
    queue = []
    for song in songs :
        if not song.lyric :
            queue.append(song)
    myjson = serializers.serialize('json', queue)
    return JsonResponse( myjson)

def add_lyrics(request):
    song_id = request.GET.get("song_id")
    lyrics = request.GET.get("song_id")
    song = Song.objects.get(song_id=song_id)
    song.lyrics = lyrics
    song.save()
    return HttpResponse(f"Lyrics for {id} added")

# def get_song_for_sentiment(request):
#     songs = Song.objects.all()
#     queue = []
#     for song in songs :
#         if not song.sentiment  :
#             queue.append(song)
#     myjson = serializers.serialize('json', queue)
#     return JsonResponse( myjson, safe=False)


# def getgenres(request):
#     user = profile.objects.get(user= request.user)
#     token = user.token
#     response = requests.get("https://api.spotify.com/v1/browse/categories",headers={"Authorization": "Bearer {}".format(token)})
#     return HttpResponse(json.dumps(response.json()), content_type = "application/json")
