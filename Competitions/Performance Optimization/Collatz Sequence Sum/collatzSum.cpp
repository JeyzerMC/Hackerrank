#include <bits/stdc++.h>

using namespace std;


// ======================================================
// int collatzSequenceLen(int n) {
//     if (n == 0) {
//         return 0;
//     }
//     if (n == 1) {
//         return 1;
//     }
//     if ((n & 1 ) == 0) {
//         return 1 + collatzSequenceLen(n >> 2);
//     }
//     return 1 + collatzSequenceLen(3*n+1);
// }

int collatzSequenceLen(int n){
    if (n <= 1)
        return n;
        
    int count = 1;

    while(n > 1){
        n = ((n & 1) == 0) ? n >> 2 : 3 * n + 1;
        count++;
    }

    return ++count;
}


// ======================================================

int main() {
    int T;
    int A;
    int B;
    cin >> T >> A >> B;
    int result = collatzSequenceSum(T, A, B);
    cout << result << endl;
    return 0;
}