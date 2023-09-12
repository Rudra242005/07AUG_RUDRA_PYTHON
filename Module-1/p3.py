a = int(input("enter A:"))
b = int(input("enter B:"))
print("A is", a)
print("b is", b)

if a != 0 and b != 0:
    if a>b:
        print("a+b",a+b)
    
    elif a<b:
        print("a-b",a-b)

    elif a==b:
        print("both are equal")
else:
    print("error")    
    