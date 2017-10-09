#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int size, nb, sum = 0;
    cin >> size;
    while(cin >> nb)
        sum += nb;
    cout << sum << endl;
    return 0;
}
