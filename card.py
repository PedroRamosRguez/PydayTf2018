#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_sugestions():
    """
        Función para obtener las sugerencias de la bienvenida al agente
    """
    sugerencias = [
        {
            'title': 'Volver a Agenda'
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
    ]
    return sugerencias
def speaker_card(tracks,images,speaker_selected):
    details = {}
    suggestions = get_sugestions()
    for i in tracks:
        for j in i['talks']:
            image = images[int(j['talk_id'])]['image']
            if j['talk_id'] == int(speaker_selected):
                details = j
                details['name'] = images[int(j['talk_id'])]['speaker']
                details['image'] = image
    simple_card = {
        'fulfillmentMessages': [
            {
                'platform': 'ACTIONS_ON_GOOGLE',
                'simpleResponses': {
                    'simpleResponses': [
                        {
                            'textToSpeech':'<speak>{name} dará su ponencia a las <say-as interpret-as="time" format="hms12">{start}</say-as><break time="600ms"/>. \n\r Hablará sobre {description}¿Qué información desea saber?</speak>'.format(
                                name = details['name'],
                                start = details['start'],
                                description = details['description']
                            ),
                            'displayText': ' ',
                        }
                    ]
                }
            },
            {
                'platform': 'ACTIONS_ON_GOOGLE',
                'basicCard': {
                    'title':details['name'],
                    'formattedText': details['description'],
                    'image': {
                        'imageUri': details['image'],
                        'accessibilityText': 'Foto {}'.format(details['name']),
                    },
                },
            },
            {
                'platform': 'ACTIONS_ON_GOOGLE',
                'suggestions': {
                    'suggestions': suggestions,
                }
            },
        ]
    }
    return simple_card