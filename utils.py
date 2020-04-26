#!/usr/bin/python

import re
import random
import datetime
from os.path import join, exists
from os import makedirs


def cargar_corpus(archivo):
    """ Carga un corpus para trabajar con él
        Recibe un nombre de archivo/ruta
        Devuelve una lista de Python
    """
    output = []
    with open(archivo,'r') as f:
        contenido = f.read()
        if ',' in contenido:
            separador = ','
        elif '\n' in contenido:
            separador = '\n'
        else:
            raise Exception("Separador desconocido para "+archivo+"\nPor favor, utiliza comas o saltos de página.")
        for palabra in contenido.split(separador):
            palabra = palabra.strip()
            if palabra != '':
                output.append(palabra)
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

def _grupo_al_azar(corpus, numero=100):
    """ Genera una lista de palabras escogidas al azar. Por defecto coge 100 palabras.
        Recibe: [1] un corpus, [2] el tamaño de la lista deseada (opcional).
        Devuelve la lista de palabras seleccionadas.
    """
    output = []
    for x in range(int(numero)):
        n = random.randint(0, (len(corpus)-1))
        output.append(corpus[n])
    return output

def guardar_sublista(lista):
    """ Guarda la sublista en disco dentro de una carpeta indicando el numero de palabras que contiene.
        Recibe: una lista de palabras
    """
    nombre_archivo = str(datetime.datetime.now()).replace(" ", "_").replace(":","-")+".txt"
    carpeta = "listas_"+str(len(lista))
    ruta = join(carpeta,nombre_archivo)
    if not exists(carpeta):
        makedirs(carpeta)
    with open(ruta,'w') as archivo:
        for palabra in lista:
            archivo.write(palabra+",")
    
def guardar_corpus(corpus):
    # Guarda el nuevo corpus
    with open('nuevo_corpus.txt','w') as archivo:
        for palabra in corpus:
            archivo.write(palabra+"\n")

    
    
    

# --------- DEPRECATED ---------------

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
