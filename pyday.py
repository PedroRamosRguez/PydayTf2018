#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from datetime import datetime
from parse_response import parse_response


def get_suggestions():
    """
        Función para obtener las sugerencias de la bienvenida al agente
    """
    sugerencias = [
        {
            'title': 'Agenda'
        },
        {
            'title': 'Ponencias Track 1'
        },
        {
            'title': 'Ponencias Track 2'
        },
        {
            'title': 'Ponencias Track 3'
        },
        {
            'title': 'Ponentes'
        },
    ]
    return sugerencias


def get_pyday_info():
    year = datetime.now().strftime("%y")
    url ='https://pythoncanarias.es/api/v1/events/pydaytf'+year +'/'
    response = requests.get(url)
    data = response.json()
    return data['result']
    
def action_pyday(req=None):
    """action de informacion del pyday
    """
    pyday_info = get_pyday_info()
    suggestions = get_suggestions()
    speech_suggestions=''.join([_['title']+'.<break time="500ms"/>\n\r' for _ in suggestions])
    talks = 0
    for i in pyday_info['tracks']:
        talks += len(i['talks'])
    speech = ''.join('''<speak>El {name} es {short_description}, <break time="600ms"/> se celebrará el 
        <say-as interpret-as="date" format="yyyymmdd" detail="1">{date}</say-as>
        <break time="600ms"/>habrán {tracks} tracks con un total de {talks} ponencias. <break time="500ms"/>
        ¿Qué información desea saber?.<break time="600ms"/> \n\r{suggestions}</speak>'''.format(
            name = pyday_info['name'],
            short_description=pyday_info['short_description'],
            date=pyday_info['start_date'],
            tracks = str(len(pyday_info['tracks'])),
            talks = talks,
            suggestions= speech_suggestions,
        ))
    text = ''.join('''El {name} es {short_description}, se celebrará el {date} habrán {tracks} tracks con un total de {talks} ponencias.
        ¿Qué información desea saber? '''.format(
            name = pyday_info['name'],
            short_description=pyday_info['short_description'],
            date=datetime.strptime(pyday_info['start_date'],'%Y-%m-%d').strftime('%d-%m-%Y'),
            tracks = str(len(pyday_info['tracks'])),
            talks = talks,
        ))
    result = {
        'fulfillmentMessages': [
            {
                'platform': 'ACTIONS_ON_GOOGLE',
                'simple_responses': {
                    'simple_responses': [
                        {
                            'text_to_speech':speech,
                            'display_text': text,
                        }
                    ]
                }
            },
            {
                'platform': 'ACTIONS_ON_GOOGLE',
                'basicCard': {
                    'image': {
                        'imageUri':'https://pythoncanarias.es/static/commons/img/logo_text-1368238e3d.png',
                        'accessibilityText': 'Logo Python Canarias',
                    },
                    "buttons": [
                        {
                            "title": "Ver en la web",
                            "openUriAction": {
                                "uri": pyday_info['url'],
                            }
                        }
                    ]
                },
            },
            {
                'platform': 'ACTIONS_ON_GOOGLE',
                'suggestions': {
                    'suggestions': suggestions
                }
            },
        ]
    }
    response = parse_response(result)
    
    return response


