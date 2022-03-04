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


### Arreglo global de resultados ###
resultados = [0] * 100


### Funcion de busqueda de palabras en el texto
def buscarPalabras(nombreLibro, palabrasABuscar, numeroHilo):
    global resultados
    print ("\nLibro: ", nombreLibro)
    resultadostmp = [0] * 10

    directorioLibro = directorioActual+'/'+nombreLibro
    file = open(directorioLibro, "r")
    fileR = file.read()
    for i in range (10):
        resultadostmp[i] = fileR.count(palabrasABuscar[i]) 
    print(resultadostmp)
    index = numeroHilo*10
    resultados[index:index+9] = resultadostmp


### Se genera un hilo por cada archivo ###
numeroHilos = 10 # Cantidad de hilos por crear
for numHilo in range(numeroHilos):
    # Argumentos: name-nombre del hilo, target-funcion que realizara, args-argumentos que recibe
    # El hilo recibe el nombre del libro que va a utilizar y las 10 palabras
    hilo = threading.Thread( name = "Hilo#%s" %numHilo, 
                            target=buscarPalabras, 
                            args=([nombresLibros[numHilo], palabrasBusqueda, numHilo]) )
    hilo.start()
        
# Trabajar hasta terminar los hilos
hilosCreados = threading.enumerate()
for numHilo in range (len(hilosCreados)-1):
	hilosCreados[numHilo+1].join()
	
print(resultados)


### El proceso padre mandará la información a la pantalla ###
print("\n ***** La info recolectada es: ***** \n")
for i in range(numeroHilos):
	print("\n*** Libro: ", nombresLibros[i])
	for j in range (10):
		indice = (i * 10) + j 
		cadena = palabrasBusqueda[j] + ": " + str(resultados)
		print (palabrasBusqueda[j]+": " + str(resultados[indice])+"\n")
		
		
