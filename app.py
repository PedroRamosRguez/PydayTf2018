#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from welcome import action_bienvenida
from pyday import action_pyday
from speakers import speakers, speakers_by_track, speakers_by_time,speaker_details
from goodbye import action_goodbye

from flask import Flask
from flask import request

# Flask app should start in global layout
app = Flask(__name__)
log = app.logger

actions = {
    'welcome': action_bienvenida,
    'pyday': action_pyday,
    'speakers': speakers,
    'speaker_details': speaker_details,
    'speakers_by_track': speakers_by_track,
    'speakers_time': speakers_by_time,
    'goodbye': action_goodbye
}

@app.route('/status', methods=['GET'])
def status():
    return 'OK'

@app.route('/static_reply', methods=['POST'])
def static_reply():
    global actions
    req = request.get_json(silent=True, force=True)
    try:
        action = req['queryResult']['action']
    except AttributeError:
        return 'json error'
    if action in actions:
        functor = actions[action]
        if functor.__doc__:
            print(functor.__doc__.split('\n')[0])
        response = functor(req)
    else:
        log.error('action unable')
    return response

if __name__ == '__main__':
    port = int(os.getenv('PORT', 50000))
    print("App running in port %d" % port)
    app.run(debug=True, port=port, host='127.0.0.1')