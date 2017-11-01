#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int arrA[3], arrB[3], nb;
    for(int i = 0; i < 3; i++){
        cin >> nb;
        arrA[i] = nb;
    }
    
    for(int i = 0; i < 3; i++){
        cin >> nb;
        arrB[i] = nb;
    }
    
    int alice = 0, bob = 0;
    
    for(int i = 0; i < 3; i++)
        if(arrA[i] < arrB[i])
            bob++;
        else if(arrA[i] > arrB[i])
            alice++;
    
    cout << alice << " " << bob << endl;
    
    return 0;
}
