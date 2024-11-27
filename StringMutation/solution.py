word = input()
index,char = input().split()

index = int(index)

word = list(word)
word[index] = char
print("".join(word))


input:
abracadabra
5 k

output:
abrackdabra
