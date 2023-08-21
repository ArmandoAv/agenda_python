import json
import os


def leer_json():
    if not os.path.isfile('../datos/datos.json'):
        with open('../datos/datos.json', 'w') as arch:
            json.dump([], arch)
    with open('../datos/datos.json', 'r') as arch:
        datos = json.load(arch)
    return datos


def escribir_json(datos):
    with open('../datos/datos.json', 'w') as arch:
        json.dump(datos, arch)


__all__ = ['leer_json', 'escribir_json']
