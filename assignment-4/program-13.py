"""Write a Python class named Circle constructed by a radius and two methods which will compute 
the area and the perimeter of a circle"""

class circle:
    
    r=int(input("enter radius of a circle : "))

    Area=3.14*r*r
    print("Area of circle : ",Area)

    perimeter=3.14*r*2
    print("Perimeter of circle : ",perimeter)

cr=circle()