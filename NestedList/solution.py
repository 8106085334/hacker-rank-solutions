if __name__ == '__main__':
    n = int(input("Enter the number of students: "))

    nested_list = []
    for i in range(n):
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))
        nested_list.append([name, score])

    # Find the lowest score
    first_min = min(stu[1] for stu in nested_list)

    # Filter out students with the lowest score
    new_list = [stu for stu in nested_list if stu[1] != first_min]

    # Find the second lowest score
    second_min = min(stu[1] for stu in new_list)

    # Find all students with the second lowest score
    new_list1 = [stu[0] for stu in new_list if stu[1] == second_min]

    # Sort the names alphabetically and print them
    new_list1.sort()
    for i in new_list1:
        print(i)
