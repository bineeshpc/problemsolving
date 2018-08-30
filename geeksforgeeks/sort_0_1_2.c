#include<stdio.h>

// https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0

int get_array(int a[], int n) {
    int i, y;
    for(i=0; i< n; i++) {
        scanf("%d", &y);
        a[i] = y;
    }
}

int sort(int a[], int n) {
    int zero_count = 0;
    int one_count = 0;
    int two_count = 0;
    int i;
    for(i=0; i<n;i++) {
        if(a[i] == 0) {
            zero_count ++;
        }else if(a[i] == 1) {
            one_count ++;
        }else if(a[i] == 2) {
            two_count ++;
        }
    }
    
        while(zero_count > 0) {
            printf("%d ", 0);
            zero_count--;
        }
        while(one_count > 0) {
            printf("%d ", 1);
            one_count--;
        }
        while(two_count > 0) {
            printf("%d ", 2);
            two_count--;
        }
  printf("\n");  
}


int swap(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int a[], int n) {
 
    /*
    
    Dutch national flag problem
    Partition the array into 0s 1s and 2s
    
    loop invariant
    everything upto a[low] is 0
    everything from a[high] to n-1 is 2
    everything from a[mid] to a[high] - 1 is yet to be processed
    
    */   
    int low, mid, high;
    low = -1;
    high = n;
    mid = 0;
    while(mid < high) {
        if(a[mid] == 0) {
            low++;
            swap(&a[low], &a[mid]);
            mid++;
        }else if(a[mid] == 2) {
            high--;
            swap(&a[mid], &a[high]);
        } else{
            mid++;
        }
    }
    
}

int printarray(int a[], int n) {
    int i;
    for(i=0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

int main() {
	//code
	int a[100];
	int t;
	int n;
	scanf("%d", &t);
	while (t > 0) {
	    scanf("%d", &n);
	    get_array(a, n);
	    //printarray(a, n);
	    //sort(a, n);
	    partition(a, n);
	    printarray(a, n);
	    t--;
	}
	return 0;
}
