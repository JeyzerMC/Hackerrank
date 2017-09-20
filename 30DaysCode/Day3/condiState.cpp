#include <string>
#include <iostream>
using namespace std;


int main(){
    int N;
    cin >> N;
    
    string msg = (N%2 == 0 && (N<6 || N>20)) ? "Not Weird" : "Weird";
    
    cout << msg << endl;
    return 0;
}
