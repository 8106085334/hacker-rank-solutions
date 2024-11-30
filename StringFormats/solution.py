n = int(input()) 
width = len(format(n,'b'))
print(width)
for i in range(1,n+1):
    decimal = str(i).rjust(width)
    octal = format(i,'o')
    hexa = format(i,'X')
    binary = format(i,'b')
    print(decimal, octal, hexa, binary) 
