#Write a Python function to reverses a string if its length is a multiple of 4.


def mystr():
    str = input("enter a string : ")
    i = len(str)
    if (i % 4) == 0 :
        print(str[-1:0])
    else:
        print(str)
    
mystr()
