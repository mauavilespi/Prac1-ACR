### Practica 1a. Conteo de Palabras
# Aviles Piña Mauricio
# Gustavo Lopez Gonzalez


# Librerias
import os # Para obtener los nombres de los libros
import threading # Para la creacion de hilos


### El proceso padre lee los nombres de los libros ###
nombresLibros = [] # Se crea un arreglo donde se guardaran los nombres
directorioActual = os.getcwd() # Obtener el directorio actual
directorioActual = directorioActual + '/Libros' # Directorio donde se guardan los libros
nombresLibros = os.listdir(directorioActual) # Se guardan los nombres de los libros
print("Directorio: \n", directorioActual)
print("Libros: \n", nombresLibros)


### Palabras a buscar ###
palabrasBusqueda = ["rey", "reina", "Dios", "caballeros", "casa", "honor", "espada", "corazon", "muerte", "bien"]


### Lista global de resultados ###
resultados = [0] * 100

### Lista global de palabras x libro
palabrasPorLibro = [0] * 10


### Funcion de busqueda de palabras en el texto
def buscarPalabras(nombreLibro, palabrasABuscar, numeroHilo):
    global resultados
    global palabrasPorLibro
    resultadostmp = [0] * 10
    directorioLibro = directorioActual+'/'+nombreLibro
    file = open(directorioLibro, "r")
    fileR = file.read()
    palabrasPorLibro[numeroHilo] = len(fileR.split())
    for i in range (10):
        resultadostmp[i] = fileR.count(palabrasABuscar[i]) 
    index = numeroHilo*10
    resultados[index:index+9] = resultadostmp


### Se genera un hilo por cada archivo ###
numeroHilos = 10 # Cantidad de hilos por crear
for numHilo in range(numeroHilos):
    # Argumentos: name-nombre del hilo, target-funcion que realizara, args-argumentos que recibe
    # El hilo recibe el nombre del libro que va a utilizar y las 10 palabras
    hilo = threading.Thread( name = "Hilo#%s" %numHilo, 
                            target= buscarPalabras, 
                            args=( [nombresLibros[numHilo], palabrasBusqueda, numHilo]) )
    hilo.start()
        

# Trabajar hasta terminar los hilos
hilosCreados = threading.enumerate()
for numHilo in range (len(hilosCreados)-1):
	hilosCreados[numHilo+1].join()
	

### El proceso padre mandará la información a la pantalla ###
print(" ***** La info recolectada es: ***** \n")


# Total de palabras x palabra a buscar
palabrasPorPalabrasBuscadas = [0] * 10


# Palabras x libro
for i in range(numeroHilos):
	print("\n*** Libro: ", nombresLibros[i])
	for j in range (10):
		indice = (i * 10) + j 
		palabrasPorPalabrasBuscadas[j] = palabrasPorPalabrasBuscadas[j] + resultados[indice]
		print (palabrasBusqueda[j]+": " + str(resultados[indice])+"\n")


# Total de palabras en todos los libros
totalPalabrasLibros = sum(palabrasPorLibro)
print("Total de palabras en los 10 libros: ", totalPalabrasLibros)


# Porcentajes
print("\n*** Porcentajes *** ")	
for j in range (10):
    porcentaje = (palabrasPorPalabrasBuscadas[j] / totalPalabrasLibros) * 100
    print (palabrasBusqueda[j]+": " + str(round(porcentaje, 3))+" %\n")