# Write a python program to sum of the first n positive integers.

a = int(input("enter n'th digit to know it's sum : "))
num =  0
for i in range(1,a+1):
    num+=i 
    
print(num)