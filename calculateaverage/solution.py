n = input("enter the integer:")
n = int(n)
new_dict = {}
for i in range(n):
    name, *list_b = input("enter the values ").split()
    list_a = list(map(int,list_b))
    new_dict[name] = list_a
query_name = input("enter the name:")

for key,value in new_dict.items():
    if query_name == key:
        l = len(value)
        sum_a = sum(value)
        avg = sum_a/l
        print(f"{avg:.2f}")
