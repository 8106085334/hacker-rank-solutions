if __name__ == '__main__':
    n = int(input("Enter the number of scores: "))
    arr = list(map(int, input("Enter the scores separated by space: ").split()))
    
    # Convert the list to a set to remove duplicates, then sort in descending order
    unique_scores = sorted(set(arr), reverse=True)
    
    # Print the second highest score
    print(unique_scores[1])
