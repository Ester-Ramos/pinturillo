# README
Este repo está para actualizar el corpus español (de España) para usar en el [pinturillo](https://skribbl.io/)

## Cómo colaboro

### De forma manual
1. Añade palabras al archivo separadas por comas. El archivo se puede modificar desde GitHub clickando en el lapiz de la esquina superior derecha cuando estás dentro del archivo.
2. Comprueba que no están repetidas: y ponla o no la pongas a tu discreción
3. Commitea los cambios en master (a lo loco)

### De forma automática
Si tienes un archivo con palabras separadas por comas, puedes utilizar `maspalabras.py`, que es un script de Python (requiere Pandas).

#### Uso
`$ python maspalabras.py <mis-lista-de-palabras>.txt`

Generará un archivo llamado corpus_nuevo.txt con las palabras añadidas y sin duplicados.

# Colaboradores

@cbmarrec

@helfio
