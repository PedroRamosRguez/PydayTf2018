#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from datetime import datetime

from card import speaker_card
from carousel import carousel_speakers_by_track, carousel_speakers_by_time
from images import list_images
from items import create_item_list, create_item_list_track,create_item_list_time
from list_response import list_speakers
from parse_response import parse_response

def get_track_time_suggestions():
    """
        Función para obtener las sugerencias de hora de tracks
    """
    sugerencias = [
        {
            'title': 'Ponencias 09:45'
        },
        {
            'title': 'Ponencias 11:00'
        },
        {
            'title': 'Ponencias 15:00'
        },
    ]
    return sugerencias
def get_speakers():
    """getting data from api
    """
    year = datetime.now().strftime("%y")
    url = 'https://pythoncanarias.es/api/v1/events/pydaytf'+ year +'/'
    response = requests.get(url)
    data = response.json()
    return data['result']['tracks']

def speakers(req=None):
    """"speakers action
    """
    tracks = get_speakers()
    images = list_images()
    items = create_item_list(tracks,images)
    result = list_speakers(items)
    response = parse_response(result)
    return response

def get_speakers_by_track(track_number):
    year = datetime.now().strftime("%y")
    url = 'https://pythoncanarias.es/api/v1/events/pydaytf'+ year +'/'
    response = requests.get(url)
    data = response.json()      
    return data['result']['tracks'][int(track_number)-1]


def speakers_by_track(req=None):
    """action speakers by track
    """
    track_number = req['queryResult']['parameters']['number']
    track = get_speakers_by_track(track_number)
    images = list_images()
    items = create_item_list_track(track,images)
    result = carousel_speakers_by_track(track_number, items)
    response = parse_response(result)
    return response


def speakers_by_time(req=None):
    """action speakers by time
    """
    track_time = req['queryResult']['parameters']['time']
    track_time = datetime.fromisoformat(track_time).strftime('%H:%M')
    tracks = get_speakers()
    images = list_images()
    items = create_item_list_time(tracks,track_time,images)
    if len(items) > 2:
        result = carousel_speakers_by_time(items,track_time)
    else:
        suggestions = get_track_time_suggestions()
        speech_suggestions=''.join([_['title']+'.<break time="500ms"/>\n\r' for _ in suggestions])
        speech = '''<speak>No hay ninguna ponencia prevista para las {} <break time="600ms"/>
        ¿Qué información desea saber? <break time="600ms"/> {}</speak>'''.format(track_time,speech_suggestions)
        text = '''No hay ninguna ponencia prevista para las {}
        ¿Qué información desea saber?'''.format(track_time)
        result = {
            'fulfillmentMessages': [
                {
                    'platform': 'ACTIONS_ON_GOOGLE',
                    'simpleResponses': {
                        'simpleResponses': [
                            {
                                'textToSpeech':speech,
                                'displayText': text,
                            }
                       ]
                    }
                },
                {
                    'platform': 'ACTIONS_ON_GOOGLE',
                    'suggestions': {
                        'suggestions': suggestions,
                    }
                },
            ],
        }
    response = parse_response(result)
    return response

def speaker_details(req=None):
    """action speaker details
    """
    speaker_selected = req['originalDetectIntentRequest']['payload']['inputs']
    speaker_selected_details = speaker_selected[0]['arguments'][0]['textValue']
    tracks = get_speakers()
    images = list_images()
    result = speaker_card(tracks,images,speaker_selected_details)
    response = parse_response(result)
    return response
