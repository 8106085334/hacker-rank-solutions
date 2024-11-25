The goal is to find the second highest score (the "runner-up") from a list of scores provided as input. The solution works as follows:

Input Handling:

The number of scores (n) is taken as input.
A list of integers (arr) is input and converted using map.
Find the Maximum:

The highest score (a) is determined using max(arr).
Remove the Maximum Scores:

The while loop ensures all occurrences of the highest score are removed from the list.
Find the Runner-Up:

Once the highest score is removed, max(arr) is called again to find the runner-up score.
inputs:
5
2 3 6 6 5
output:
5
