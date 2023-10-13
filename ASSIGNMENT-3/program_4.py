#Write a Python program to check a list is empty or not.

l = []
n = int(input("enter number of list members : "))
for k in range(n):
    x = input("enter list members : ")
    l.append(x)

for i in l:
    print(l)
if len(l)==0:
    print("list is empty...")
else:
    print("list is not empty...")

