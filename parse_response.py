#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
from flask import make_response


def parse_response(result):
    """
        Función para parsear la respuesta que se devuelve en formato json al lado cliente
    """
    res = json.dumps(result)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r