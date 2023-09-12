#Write a Python program to get the Fibonacci series of given range.

r = int(input("enter a number for fibonacci series : "))

f = 0
f1 = 1

for i in range(r+1):
    f,f1 = f1,f+f1
print(f1)