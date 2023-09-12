#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("enter a value : "))
b = int(input("enter a value : "))
c = int(input("enter a value : "))

print(f"you entered {a} {b} {c}")

if a==b or b==c or a==c :
    print("0")
    print("error! re enter the values properly.")
else:
    print(f"sum of your entered values {a+b+c}")