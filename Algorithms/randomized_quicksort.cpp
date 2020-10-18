#include <iostream>
using namespace std;

void swap(int *a,int *b){
	int temp = *b;
	*b = *a;
	*a = temp;
}

int random_partition(int a[],int start,int end){
	srand(time(NULL)); 
    int random = start + rand() % (end - start); 
    swap(&a[random], &a[end]);

	int pivot = a[end];
	int pindex = start;
	for(int i = start; i < end ; i++){
		if(a[i] <= pivot){
			swap(&a[i],&a[pindex]);
			pindex++;
		}
	}
	swap(&a[pindex],&a[end]);

	return pindex;
}
void randomized_quicksort(int a[],int start,int end){
	if(start < end){
		int pindex = random_partition(a,start,end);
		randomized_quicksort(a,start,pindex-1);
		randomized_quicksort(a,pindex+1,end);
	}
}
int main(){
	int n;
	cin >> n;
	int a[n];

	for(int i = 0 ; i < n ; i++){
		cin >> a[i];
	}

	randomized_quicksort(a,0,n-1);

	for(int i = 0 ; i < n ; i++){
		cout << a[i] << " ";
	}
	cout << endl;
}