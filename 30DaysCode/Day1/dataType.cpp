#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";
    
    // Declare second integer, double, and String variables.
    int j;
    double k;
    string line;
    // Read and save an integer, double, and String to your variables.
    getline(cin, line);
    j = stoi(line);

    getline(cin, line);
    k = stod(line);
    getline(cin, line);
    // Print the sum of both integer variables on a new line.
    cout << i + j << endl;
    // Print the sum of the double variables on a new line.
    cout << fixed << setprecision(1) << d + k << endl;
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    cout << s + line << endl;
    return 0;
}