"""Write a Python function that takes two lists and returns true if they have at least one common member."""

list_1 = []
list_2 = []
n = int(input("enter number of members for list_1 : "))

for i in range(n):
    x = int(input("enter members for list_2 : "))
    list_1.append(x)

m = int(input("enter number of members for list_2: "))

for i in range(m):
    x = int(input("enter members for list_2 : "))
    list_2.append(x)
print(list_1)
print(list_2)
common_list=[]
for elements in list_1:
    if elements in list_2:
        
        common_list.append(elements)

print(common_list)