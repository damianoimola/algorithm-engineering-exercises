#include <stdio.h>
#include <stdio.h>

int binary_search(int n, int * arr);

int main(int argc, char * argv[]){
	int n = argc-1;
	int * arr = (int *) malloc(n*sizeof(int));
	for(int i=0; i<n; i++){
		arr[i] = atoi(argv[i+1]);
	}

	int res = binary_search(n, arr);
	printf(res == -1 ? "Non trovato" : "Il valore è in posizione %d", res);
} 
