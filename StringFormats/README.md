This Python program takes an integer n as input and prints the decimal, octal, hexadecimal, and binary representations
 of all integers from 1 to n. Each of the representations is aligned with the maximum width needed 
for the binary format of n.

Features
Takes an integer n as input.
Outputs four columns: Decimal, Octal, Hexadecimal, and Binary representations.
Each value is aligned to ensure consistent column width.
Supports formatting with .rjust() to maintain the output's structure.
Usage
Clone or download the repository.
Run the Python script.

Input:
5

Output:
  1  1  1  1
  2  2  2  10
  3  3  3  11
  4  4  4  100
  5  5  5  101
Code Explanation:
Input: The program accepts an integer n from the user.
Width Calculation: The maximum width for formatting is determined based on the binary representation of n.
Loop: For every number from 1 to n, the program calculates:
Decimal representation (right-justified).
Octal representation.
Hexadecimal representation (uppercase).
Binary representation.
Output: Each of the four formats is printed in a neat, aligned manner.
