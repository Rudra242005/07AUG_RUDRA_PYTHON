#Write a Python program to split a list into different variables.

list = [1,65,89,321,000]
str = ""
for i in list:
   v = i
   v = input(f"Enter value of variable of {i}:")
   print(f"{i}=",v)