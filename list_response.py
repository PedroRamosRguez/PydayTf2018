#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_sugestions():
    """
        Función para obtener las sugerencias de la bienvenida al agente
    """
    sugerencias = [
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


def list_speakers(items):
    suggestions = get_sugestions()
    names= ''.join([_['title']+ '\n\r <break time="600ms"/> con su ponencia titulada '+_['description']+'<break time="600ms"/>' for _ in items])
    result = {
        'fulfillmentMessages': [
            {
                'platform': 'ACTIONS_ON_GOOGLE',
                'simpleResponses': {
                    'simpleResponses': [
                        {
                            'textToSpeech': '<speak>Este es el listado de ponentes del PyDay <break time="600ms"/> {} </speak>'.format(names),
                            "displayText": ' ',
                        }
                    ]
                }
            },
            {
                'platform': 'ACTIONS_ON_GOOGLE',
                'listSelect':{
                    'title': 'Listado de ponentes del Pyday',
                    'items':items
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
    return result