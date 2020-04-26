# README
Este repo está para actualizar el corpus español (de España) para usar en el [pinturillo](https://skribbl.io/)

## Cómo colaboro

### De forma manual
1. Añade palabras al archivo, una por línea. El archivo se puede modificar desde GitHub clickando en el lapiz de la esquina superior derecha cuando estás dentro del archivo.
2. Comprueba que no están repetidas: y ponla o no la pongas a tu discreción
3. Commitea los cambios en master (a lo loco)

### De forma automática
Si tienes un archivo con palabras separadas por comas, puedes utilizar `maspalabras.py`, que es un script de Python.

#### Uso
`$ python maspalabras.py <mis-lista-de-palabras>.txt`

Generará un archivo llamado corpus_nuevo.txt con las palabras añadidas y sin duplicados.

## Cómo generar listas de palabras
`$ python generador.py <nº de listas> <longitud de las listas>`

Donde `<nº de listas>` es el número de listas que se quieren generar y `<longitud de las listas>` es el número de palabras de cada lista.

# Colaboradores

@cbmarrec

@helfio
