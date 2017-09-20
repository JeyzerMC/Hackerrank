using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        int i = 4;
        double d = 4.0;
        string s = "HackerRank ";
        
        // Declare second integer, double, and String variables.
        int j = Convert.ToInt32(Console.ReadLine());
        // Read and save an integer, double, and String to your variables.
        double k = Convert.ToDouble(Console.ReadLine());
        string line = Console.ReadLine();
        // Print the sum of both integer variables on a new line.
        Console.WriteLine(i + j);
        Console.WriteLine($"{d + k:0.0#}",d + k);
        Console.WriteLine(s + line);
        // Print the sum of the double variables on a new line.
        
        // Concatenate and print the String variables on a new line
        // The 's' variable above should be printed first.
    }
}