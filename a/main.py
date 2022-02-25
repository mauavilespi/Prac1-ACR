# Librerias
import os # Para obtener los nombres de los libros

### El proceso padre lee los nombres de los libros ###
nombresLibros = [] # Se crea un arreglo donde se guardaran los nombres
directorioActual = os.getcwd() # Obtener el directorio actual
directorioActual = directorioActual + '/a/Libros' # Directorio donde se guardan los libros
nombresLibros = os.listdir(directorioActual) # Se guardan los nombres de los libros
print("Directorio: \n", directorioActual)
print("Libros: \n", nombresLibros)