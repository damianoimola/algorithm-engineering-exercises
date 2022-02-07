#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <time.h>

void ptrprnt(char * msg, int n, int * ptr);
void insertion_sort(int n, int * arr);
void rndptr(int n, int * arr);

int main(int argc, char * argv[]){
	assert(argc == 2);
	int n = atoi(argv[1]);

	int * arr = (int*) malloc(n*sizeof(int));
	rndptr(n, arr);
	ptrprnt("Array prima dell'ordinamento", n, arr);
	insertion_sort(n, arr);
	ptrprnt("Array dopo dell'ordinamento", n, arr);
	free(arr);
}


void rndptr(int n, int * arr){
	srand(time(NULL));
	for(int i=0; i<n; i++){
		arr[i] = (double)rand() / RAND_MAX * 100;
	}
}

void insertion_sort(int n, int * arr){
	for(int i=1; i<n; i++){
		int tmp = arr[i];
		int j = i;
		while(j>1 && arr[j-1]>tmp){
			arr[j] = arr[j-1];
			j = j-1;
		}
		arr[j] = tmp;
	}
}

void ptrprnt(char * msg, int n, int * ptr){
	printf("%s --> ", msg);
	for(int i=0; i<n; i++){
		printf("%d, ", ptr[i]);
	}
	printf("\b\b\n");
}
