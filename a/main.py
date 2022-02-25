# Librerias
import os # Para obtener los nombres de los libros
import threading # Para la creacion de hilos

### El proceso padre lee los nombres de los libros ###
nombresLibros = [] # Se crea un arreglo donde se guardaran los nombres
directorioActual = os.getcwd() # Obtener el directorio actual
directorioActual = directorioActual + '/a/Libros' # Directorio donde se guardan los libros
nombresLibros = os.listdir(directorioActual) # Se guardan los nombres de los libros
print("Directorio: \n", directorioActual)
print("Libros: \n", nombresLibros)


### Palabras a buscar ###
# El usuario las puede escoger via terminal o podemos definirlas con la variable "palabrasBusqueda"
palabrasBusqueda = ["rey", "princesa", "sapo", "cueva", "casa", "piedra", "cielo", "corazon", "volcan", "perro"]


### Funcion de busqueda de palabras en el texto
def buscarPalabras(nombreLibro, palabrasABuscar):
    print ("Libro: ", nombreLibro)
    print ("Palabras a buscar: ", palabrasABuscar)


### Se genera un hilo por cada archivo ###
numeroHilos = 10 # Cantidad de hilos por crear
for numHilo in range(numeroHilos):
    # Argumentos: name-nombre del hilo, target-funcion que realizara, args-argumentos que recibe
    # El hilo recibe el nombre del libro que va a utilizar y las 10 palabras
    hilo = threading.Thread( name = "Hilo#%s" %numHilo, 
                            target=buscarPalabras, 
                            args=(nombresLibros[numHilo], palabrasBusqueda) )
    hilo.start()