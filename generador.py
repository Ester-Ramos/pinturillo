#!/usr/bin/python

import sys
import utils


def generador(numero, longitud=100):
    corpus = utils.cargar_corpus('corpus.txt')
    for x in range(int(numero)):
        lista = utils._grupo_al_azar(corpus, longitud)
        utils.guardar_sublista(lista)


if __name__ == '__main__':
    argumentos = sys.argv
    longitud = 100
    if len(argumentos) == 1:
        print("Por favor, Dime al menos cuántas listas quieres que genere.")
        sys.exit(0)
    elif len(argumentos) == 2:
        generador(argumentos[1])
        print("¡Gracias, ahí tienes tus {} listas de 100 palabras!".format(argumentos[1]))
    elif len(argumentos) == 3:
        generador(argumentos[1], argumentos[2])
        print("¡Gracias, ahí tienes tus {} listas de {} palabras!".format(argumentos[1], argumentos[2]))
    else:
        print("""No sé qué hacer con más de dos parámetros.
Por favor, echa un ojo a mi forma de funcionar:
        $ python generador.py <nº de listas> <longitud de las listas>
    <nº de listas> es un número entero e indica cuántas listas quieres que genere.
    <longitud de las listas> también es un número entero, es opcional y me indica cuántas palabras quieres que incluya en cada lista.
""")
        sys.exit(0)
    
