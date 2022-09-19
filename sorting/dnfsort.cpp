#include <iostream>
 
using namespace std;

void swap(int arr[], int a, int b){
    int t = arr[a];
    arr[a] = arr[b];
    arr[b] = t;
}

void dnfSort(int arr[], int n){
    int low, mid = 0, 
    high = n - 1;

    while(mid <= high){
        if(arr[mid] == 0){
            swap(arr, low, mid);
            low++;
            mid++;
        } else if (arr[mid] == 2){
            swap(arr, mid, high);
            high--;
        } else {
            mid++;
        }
    }
}


int main(){

    int arr[] = {2, 2, 1, 2, 0, 0, 0, 1, 0, 2, 0, 1};

    dnfSort(arr, 12);

    for(int i = 0; i < 12; i++){
        cout << arr[i] << " ";
    }

    return 0;
}