#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from parse_response import parse_response

def get_sugestions():
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

def action_bienvenida(req=None):
    """action de bienvenida
    """
    welcome_sugestions = get_sugestions()
    sugestion_message = ["<break time='500ms'/>"+str(i['title']) for i in welcome_sugestions]
    welcome_message = '''
        ¡Hola! Bienvenido a CanPy, tu agente para el evento del PyDay
        ¿Qué información desea saber?
    '''
    welcome_message_speech = '''<speak><emphasis level='strong'>
        ¡Hola! Bienvenido a <lang xml:lang="en">CanPy</lang>, tu agente para el evento del PyDay.
        ¿Qué información desea saber?
    '''
    for i in sugestion_message:
        welcome_message_speech = welcome_message_speech + str(i) + ','
    welcome_message_speech = welcome_message_speech + '''</emphasis></speak>'''
    result = {
        'fulfillmentMessages': [
            {
                'platform': 'ACTIONS_ON_GOOGLE',
                'simpleResponses': {
                    'simpleResponses': [
                        {
                            'textToSpeech': welcome_message_speech,
                            "displayText": welcome_message,
                        }
                    ]
                }
            },
            {
                'platform': 'ACTIONS_ON_GOOGLE',
                'suggestions': {
                    'suggestions': welcome_sugestions,
                }
            },
        ],
    }
    response = parse_response(result)
    return response