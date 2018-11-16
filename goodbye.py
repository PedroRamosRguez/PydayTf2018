#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from parse_response import parse_response

def action_goodbye(reques=None):
    """action goodbye"""
    result = {
        'fulfillmentMessages': [
            {
                'platform': 'ACTIONS_ON_GOOGLE',
                'simpleResponses': {
                    'simpleResponses': [
                        {
                            'textToSpeech': 'Gracias por utilizar Can Pai, happy Coding',
                            "displayText": 'Gracias por utilizar CanPy. Happpy Coding',
                        }
                    ]
                }
            },
        ],
    }
    response = parse_response(result)
    return response