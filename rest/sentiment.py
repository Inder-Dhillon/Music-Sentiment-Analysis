#!/usr/bin/env python3 

import django
import os
import sys
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest.settings")
django.setup()
from hackfest.models import Song

from monkeylearn import MonkeyLearn
import requests
import json
model_id = 'cl_pi3C7JiL'
ml = MonkeyLearn('824aa84b7a928c67a9d38219a751d748feef1ffc')

def get_sentiment():
    songs = Song.objects.all()
    for song in songs :
        if not song.sentiment and song.lyric > "" :
            data = [song.lyric]
            result = ml.classifiers.classify(model_id, data)
            classifications  = result.body[0]["classifications"][0]
            sentiment  = classifications["tag_name"]
            confidence  = classifications["confidence"]
            song.sentiment = sentiment
            song.magnitude = confidence
            song.save()
            print(classifications)
    
if __name__ == "__main__":
    get_sentiment()
