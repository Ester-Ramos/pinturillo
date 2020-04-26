#!/usr/bin/python

import sys
import utils

if __name__ == '__main__':
    argumentos = sys.argv
    if len(argumentos) == 1:
        print("Por favor, dame una lista de palabras a añadir")
        sys.exit(0)
    elif len(argumentos) > 2:
        print("Por favor, dame las listas de palabras de una en una")
        sys.exit(0)
    else:
        print("¡Gracias, qué buena gente eres!")

    # Cargamos el corpus actual
    corpus = utils.cargar_corpus('corpus.txt')

    # Elimina duplicados existentes en el corpus
    corpus = utils.elimina_duplicados(corpus)

    # Cargamos la lista nueva
    palabras_nuevas = utils.cargar_corpus(argumentos[1])
    
    # Si tiene duplicados, los eliminamos
    palabras_nuevas = utils.elimina_duplicados(palabras_nuevas)

    # Finalmente, añadimos las palabras:
    corpus = utils.incluir_lista(corpus, palabras_nuevas)
    
    # Escribimos el archivo con _nuevo en el nombre.
    with open('corpus_nuevo.txt','w') as archivo:
        archivo.write(", ".join(corpus))
