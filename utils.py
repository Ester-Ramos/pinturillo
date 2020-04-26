#!/usr/bin/python

import pandas as pd
import re


def elimina_duplicados(corpus):
    """ Elimina palabras duplicadas en el corpus. Utiliza una expresión regular que busca .1, .2, .3, etc
        Recibe una lista de Python
        Devuelve una lista de Python
     """
    duplicadoRe = re.compile(r"\w+\.[0-9]")
    nuevo_corpus = []
    for palabra in corpus:
        if duplicadoRe.fullmatch(palabra):
            print("Eliminando palabra duplicada:", palabra.split(".")[0])
        else:
            nuevo_corpus.append(palabra)
    return nuevo_corpus

def cargar_corpus(archivo):
    """ Carga un corpus con Pandas para trabajar con él
        Recibe un nombre de archivo/ruta
        Devuelve una lista de Python. Los duplicados llevan un .X con X = 1,2,3...
    """
    return [x.strip() for x in pd.read_csv(archivo).columns]

def incluir_lista(corpus, palabras_nuevas):
    """ Añade las palabras nuevas al corpus.
        Recibe: [1] un corpus, [2] una lista de palabras a añadir
        Devuelve el corpus con las palabras incluidas evitando duplicados.
    """
    for palabra in palabras_nuevas:
        if palabra not in corpus:
            corpus.append(palabra)
    return corpus
