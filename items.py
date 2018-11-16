#!/usr/bin/env python3
# -*- coding: utf-8 -*-

new_talks_track1 = [
    {
        'talk_id':7,'name':'Objetos hashables','start':'09:45','end':'10:55',
        'description':'''Las tablas hash son la estructura de datos más importante 
        conocida por la humanidad y lo que Python usa internamente para implementar 
        dicts y sets. A fin de poder usar nuestras propias clases como claves de un 
        diccionario o miembros de un conjunto, éstas han de ser hashables. La documentación 
        de Python nos explica cómo hacerlo: tan sólo necesitamos implementar en nuestra 
        clase los métodos __hash__() y __eq__() — o, si lo preferimos, __cmp__(). 
        Hacer eso basta para que, por ejemplo, podamos definir un set de objetos de 
        nuestra recién definida clase Perro.'''
    },
    {
        'talk_id':12,'name':'Oh, vosotros, los que entráis, abandonad toda esperanza',
        'start':'18:05','end':'19:15','description':'''Como programadores de Python, 
        estamos acostumbrados a usar nuestro lenguaje favorito continuamente pero alguna 
        vez que otra pasa por nuestra cabeza la duda de cómo funciona todo esto. ¿Cómo 
        está implementado un lenguaje de programación? ¿Cómo sabe Python si lo que escribo
        es correcto o no? ¿Cómo se transforma y ejecuta el código que escribimos?
        El objetivo de esta charla es aprender todo lo posible acerca de sintaxis,
        gramática, árboles sintácticos abstractos, como un lenguaje como Python funciona
        y cómo CPython (la implementación por defecto del intérprete) en particular está 
        implementado. Para que la sesión no sea simplemente una serie de diatribas teóricas,
        utilizaremos la excusa de modificar, retorcer y extender la gramática de Python como
        hilo conductor para entender cómo todas las piezas encajan y para aprender cómo 
        funcionan todas las técnicas avanzadas de análisis y modificación de código. Para 
        ello empezaremos hablando de cómo modificar código de Python modificando su árbol 
        sintáctico abstracto y veremos algunos ejemplos de librerías (pytest, 2to3…) 
        que utilizan esta técnica. Después veremos como extender la gramática de Python 
        "informalmente" utilizando un códec personalizado y qué aplicaciones podría tener esto.
        Finalmente hablaremos de cómo modificar realmente la gramática de Python creando 
        nuestro propio intérprete modificado en caso de que algún día queramos implementar 
        nuestro propio lenguage o modificar el propio Python. Tras terminar la charla 
        ganaremos conocimiento de como funciona Python y, por extensión, otros lenguajes 
        de programación además de tener un montón de malas ideas inmantenibles en mente para
        la próxima vez que queramos asustar a nuestros compañeros programadores.'''
    }
]
def create_item_list(tracks,images):
    items=[]
    tracks[0]['talks'].extend(new_talks_track1)
    for i in tracks:
        for j in i['talks']:
            image = images[int(j['talk_id'])]['image']
            items.append({
                'info': {
                    'key': '{}'.format(str(j['talk_id'])),
                    'synonyms': [
                        'sinonimo {}'.format(str(j['talk_id'])),
                        'ver informacion sobre la ponencia {}'.format(str(j['talk_id']))
                    ]
                },
                'title': images[int(j['talk_id'])]['speaker'],
                'description': j['name'],
                'image': {
                    'imageUri':  image,
                    'accessibilityText': 'Foto '+images[int(j['talk_id'])]['speaker'],
                },
            })
    return items
    

def create_item_list_track(tracks,images):
    items=[]
    if tracks['track_id'] == 1:
        tracks['talks'].extend(new_talks_track1)
    for _ in tracks['talks']:
        image = images[int(_['talk_id'])]['image']
        items.append({
            'info': {
                'key': '{}'.format(str(_['talk_id'])),
                'synonyms': [
                    'sinonimo {}'.format(str(_['talk_id'])),
                    'ver informacion sobre la ponencia {}'.format(str(_['talk_id']))
                ]
            },
            'title': images[int(_['talk_id'])]['speaker'],
            'description': _['name'],
            'image': {
                'imageUri':  image,
                'accessibilityText':  'Foto '+images[int(_['talk_id'])]['speaker'],
            },
        })
    return items

def create_item_list_time(tracks,time,images):
    items=[]
    tracks[0]['talks'].extend(new_talks_track1)
    for i in tracks:
        for j in i['talks']:
            if j['start'] == time:
                print(j['talk_id'])
                image = images[int(j['talk_id'])]['image']
                print(image)
                items.append({
                    'info': {
                        'key': '{}'.format(str(j['talk_id'])),
                        'synonyms': [
                            'sinonimo {}'.format(str(j['talk_id'])),
                            'ver informacion sobre la ponencia {}'.format(str(j['talk_id']))
                        ]
                    },
                    'title': images[int(j['talk_id'])]['speaker'],
                    'description': j['name'],
                    'image': {
                        'imageUri':  image,
                        'accessibilityText': 'Foto '+images[int(j['talk_id'])]['speaker'],
                    },
                })
    return items