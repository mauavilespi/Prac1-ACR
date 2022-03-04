#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int numeroHilos, filasA, columnasA, filasB, columnasB;
int **matA;
int **matB;
int **matC;

struct Rango{
	int filaInicio;
	int filaFin;
};

/*
*	Funcion que se convertira en hilo.
*	Hace los calculos de multiplicacion de matrices.
*/
void *calculo(void *rango){
	struct Rango *r = (struct Rango *) rango;

	int aux=0;
	for(int k = r->filaInicio;k <= r->filaFin;k++){
		for(int i = 0;i < columnasB;i++){
			for(int j=0; j < columnasA;j++)
				aux+=matA[k][j]*matB[j][i];
			matC[k][i] = aux;
			aux = 0;
		}
		aux = 0;
	}
}

int **generarMatriz(int *filas, int *columnas){
	int **matriz = (int **) malloc(sizeof(int *) * (*filas));
	for(int i=0; i < *filas; i++)
		matriz[i] = (int *) malloc(sizeof(int) * (*columnas));
	return matriz;
}

void llenarMatriz(int *filas, int *columnas, int **matriz){
	//Inicializa las posiciones de una matriz con valores entre el 0 y 4
	matriz[0][0]=0;
	for(int i=0; i < *filas; i++)
		for(int j=0; j < *columnas; j++)
			matriz[i][j] = rand()%5;
}

void imprimirMatrices(){
	printf("\nMatriz A\n");
	for(int i=0; i < filasA; i++){
		for(int j=0; j < columnasA; j++)
			printf(" %d ",matA[i][j]);
		printf("\n");
	}

	printf("\nMatriz B\n");

	for(int i=0; i < filasB; i++){
		for(int j=0; j < columnasB; j++)
			printf(" %d ",matB[i][j]);
		printf("\n");
	}

	printf("\nMatriz C\n");

	for(int i=0; i < filasA; i++){
		for(int j=0; j < columnasB; j++)
			printf(" %d ",matC[i][j]);
		printf("\n");
	}
}

/*
*	./B.o FilasA ColumnasA FilasB ColumnasB NumHilos
*/
int main(int argc, char **argv){
	//Inicia validacion de argumentos
	if(argc != 6){
		printf("Error: Ingrese todos los argumentos.\n");
		printf("Uso: ./B.o FilasA ColumnasA FilasB ColumnasB NumHilos\n");
		exit(1);
	}

	numeroHilos = atoi(argv[5]);
	filasA = atoi(argv[1]);
	columnasA = atoi(argv[2]);
	filasB = atoi(argv[3]);
	columnasB = atoi(argv[4]);

	if(filasB != columnasA){
		printf("Error: Numero de filas de la matriz A debe ser el mismo que las columnas de la matriz B.\n");
		exit(1);
	}

	if(numeroHilos > filasA){
		printf("Error: Debe especificar menos hilos que filas de la matriz A.\n");
		exit(1);
	}
	//Finaliza validacion de argumentos

	//Reservar memoria para las matrices
	matA = generarMatriz(&filasA,&columnasA);
	matB = generarMatriz(&filasB,&columnasB);
	matC = generarMatriz(&filasA,&columnasB);

	//Inicializar matrices
	llenarMatriz(&filasA,&columnasA,matA);
	llenarMatriz(&filasB,&columnasB,matB);

	imprimirMatrices();

	//Generar los hilos
	int filasXHilo = filasA / numeroHilos;
	pthread_t *arrHilo;
	arrHilo = (pthread_t *) malloc(sizeof(pthread_t) * numeroHilos);
	struct Rango *r;
	r = (struct Rango *) malloc(sizeof(struct Rango)*numeroHilos);

	for (int i = 0, j = 0; i < numeroHilos; i++, j+=filasXHilo){
		//Algoritmo para decidir el numero de filas de cada hilo
		r[i].filaInicio = j;
		r[i].filaFin = j + filasXHilo - 1;

		if((i+1)==numeroHilos)
			r[i].filaFin += filasA % numeroHilos;
		
		if (pthread_create(&arrHilo[i], NULL, calculo, (void *) &r[i]) < 0){
			printf("No se pudo crear el hilo\n");
			exit(1);
		}
	}

	for(int j=0;j<numeroHilos;j++){
        pthread_join(arrHilo[j],NULL);
    }

	free(arrHilo);
	free(r);

	imprimirMatrices();

	return 0;
}