"""Write a Python class named Rectangle constructed by a length and width and 
a method which will compute the area of a rectangle"""

class rectangle:
    length=int(input("enter length of a rectangle: "))
    width=int(input("enter width of a rectangle: "))

    area = length*width
    print("Area of reactangle is : ",area)

re = rectangle()