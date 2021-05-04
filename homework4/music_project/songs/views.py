from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse, HttpResponseNotFound

library = {}

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def save_song(request):
    if request.method == 'POST':
        print(request.body)
        song = json.loads(request.body)
        id = song['song_id']
        del song['song_id']
        library[id] = song
        print(library)
        return JsonResponse({'status':'success'})

def get_songs(request):
    if request.method == 'GET':
        songs = []
        print(library.values())
        for obj in library.values():
             songs.append({'name': obj['name'], 'artist': obj['artist']})
        return JsonResponse({'songs': songs})


def song_info(request, song_id):
    if request.method == 'GET':
        try:
            song_info = library[song_id]
        except:
            return HttpResponseNotFound('<h1>Song is not in the library</h1>')
        return JsonResponse({'song_id': song_id, 'info': song_info})
