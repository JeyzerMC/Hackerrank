#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    int nb;
    cin >> nb;
    cin.ignore();
    
    string sentence, wordOne, wordTwo;
    
    for(size_t i = 0; i < nb; i++){
        wordOne = wordTwo = "";
        getline(cin, sentence);
        for(size_t j = 0; j < sentence.length(); j++){
            if(j%2 == 0)
                wordOne += sentence[j];
            else
                wordTwo += sentence[j];
        }
        
        cout << wordOne << " " << wordTwo << endl;
    }
    return 0;
}
