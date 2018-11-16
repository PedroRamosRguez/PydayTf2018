#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def carousel_speakers_by_track(track,items):
    names= ''.join([_['title']+ '\n\r <break time="600ms"/>' for _ in items])
    result = {
            'fulfillmentMessages': [
                {
                    'platform': 'ACTIONS_ON_GOOGLE',
                    'simpleResponses': {
                        'simpleResponses': [
                            {
                                'textToSpeech':'<speak>Estos son los ponentes del track {} <break time="600ms"/>{} </speak>'.format(str(int(track)),names),
                                'displayText': 'Estos son los ponentes del track {}'.format(str(int(track))),
                            }
                        ]
                    }
                },
                {
                    'platform': 'ACTIONS_ON_GOOGLE',
                    'carouselSelect': {
                        'items': [_ for _ in items]
                    },
                },
            ],
        }
    return result


def carousel_speakers_by_time(items,time):
    names= ''.join([_['title']+ '\n\r <break time="600ms"/>' for _ in items])
    result = {
            'fulfillmentMessages': [
                {
                    'platform': 'ACTIONS_ON_GOOGLE',
                    'simpleResponses': {
                        'simpleResponses': [
                            {
                                'textToSpeech':'<speak> Estos son los ponentes de las <say-as interpret-as="time" format="hms12">{}</say-as> <break time="600ms"/>{}</speak>'.format(str(time),names),
                                'displayText': 'Estos son los ponentes de las {}'.format(str(time)),
                            }
                        ]
                    }
                },
                {
                    'platform': 'ACTIONS_ON_GOOGLE',
                    'carouselSelect': {
                        'items': [_ for _ in items]
                    },
                },
            ],
        }
    return result