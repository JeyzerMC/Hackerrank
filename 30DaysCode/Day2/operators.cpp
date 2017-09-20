#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    float mealCost;
    cin >> mealCost;
    
    float tipPercent;
    cin >> tipPercent;
    
    float taxPercent;
    cin >> taxPercent;
    
    float cost = round(mealCost + mealCost * tipPercent / 100 + mealCost * taxPercent / 100);
    
    cout << "The total meal cost is " << (int)cost << " dollars." << endl;
    return 0;
}
