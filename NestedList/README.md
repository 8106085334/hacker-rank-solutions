# Nested List Problem

This solution identifies the names of students with the second lowest scores in a list of student records. If there are multiple students with the same second lowest score, their names are printed in alphabetical order.

## Problem Description

You are given a list of student records, where each record contains:
1. A student's name (string).
2. A student's score (float).

The goal is to:
1. Find the second lowest score.
2. Identify all students with that score.
3. Print their names in alphabetical order.

### Input
1. An integer `n`, the number of students.
2. For each student:
   - A string (name).
   - A float (score).

### Output
The names of students with the second lowest score, printed in alphabetical order.

### Example

#### Input:
5 Harry 37.21 Berry 37.21 Tina 37.2 Akriti 41 Harsh 39
#### Output:
Berry Harry


---

## Approach

1. **Parse Input:**
   - Collect student names and scores into a nested list.

2. **Find the Minimum Score:**
   - Identify the lowest score in the list.

3. **Filter the List:**
   - Remove students with the lowest score.

4. **Find the Second Lowest Score:**
   - Calculate the minimum score from the remaining list.

5. **Identify Matching Students:**
   - Find all students with the second lowest score and sort their names alphabetically.

---

## Usage

To run the solution:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/coding-challenges.git
   cd coding-challenges/nested_list

