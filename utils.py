#!/usr/bin/python

import re


def cargar_corpus(archivo):
    """ Carga un corpus para trabajar con él
        Recibe un nombre de archivo/ruta
        Devuelve una lista de Python
    """
    output = []
    with open(archivo,'r') as f:
        for palabra in f.read().split(','):
            output.append(palabra.strip())
    return output
        
    
def elimina_duplicados(corpus):
    """ Elimina palabras duplicadas en el corpus
        Recibe una lista de Python
        Devuelve una lista de Python con el corpus ordenado por orden alfabetico
     """
    return sorted(list(set(corpus)))

def incluir_lista(corpus, palabras_nuevas):
    """ Añade las palabras nuevas al corpus.
        Recibe: [1] un corpus, [2] una lista de palabras a añadir
        Devuelve el corpus con las palabras incluidas evitando duplicados.
    """
    for palabra in palabras_nuevas:
        if palabra not in corpus:
            corpus.append(palabra)
    return corpus

def elimina_duplicados_legacy(corpus):
    """ DEPRECATED: Elimina palabras duplicadas en el corpus. Utiliza una expresión regular que busca .1, .2, .3, etc
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

def cargar_corpus_legacy(archivo):
    """ DEPRECATED: Carga un corpus con Pandas para trabajar con él
        Recibe un nombre de archivo/ruta
        Devuelve una lista de Python. Los duplicados llevan un .X con X = 1,2,3...
    """
    import pandas as pd
    return [x.strip() for x in pd.read_csv(archivo).columns]
