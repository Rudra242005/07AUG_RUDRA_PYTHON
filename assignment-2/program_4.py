# Write python program that swap two number with temp variable and without temp variable.


a = int(input("enter first number : "))
b = int(input("enter second number : "))
print("with temporary variables")

c = a
a = b
b = c 
print(f"after swap first number is {a}")
print(f"after swap second number is {b}")

print("without temporary veriales")
a,b = b,a
print("first value is ",a)
print("second value is ",b)
