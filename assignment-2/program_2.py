# Write a Python program to get the Factorial number of given number.

a = int(input("enter a number to know it's factorial :"))
fact = 1
for i in range(1,a+1):
    fact*=i
    
print(fact)


