<?php
// Declare second integer, double, and String variables.
$j = fgets($handle);
// Read and save an integer, double, and String to your variables.
$k = fgets($handle);
$line = fgets($handle);
// Print the sum of both integer variables on a new line.

echo $i + $j;
echo "\n";
// Print the sum of the double variables on a new line.
echo number_format((float)$d + $k, 1, '.', ''); 
echo "\n";

//fwrite(STDOUT, $d + $k);
//fwrite(STDOUT, "\n");
// Concatenate and print the String variables on a new line
// The 's' variable above should be printed first.

echo $s.$line;
?>