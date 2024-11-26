Average Calculator for User Data
This Python script allows users to input a number of entries containing a name and a list of integers (e.g., scores). It stores the data in a dictionary and calculates the average of the integers associated with a given name when queried.

Features
Accepts multiple entries of names and associated numeric values.
Computes the average of the numeric values for a queried name.
Provides a formatted output with the average up to two decimal places.
How It Works
The user specifies the number of entries they want to input.
For each entry, the user provides a name followed by a series of integers separated by spaces.
The script stores this data in a dictionary where:
Key: The name (string).
Value: A list of integers.
The user can then query the dictionary by providing a name to compute and display the average of its associated integers.
Input Example
Enter the integer: 3
Enter the values: Alice 70 85 90
Enter the values: Bob 88 92 77
Enter the values: Charlie 60 75 80
Enter the name: Bob
Output Example
85.67
