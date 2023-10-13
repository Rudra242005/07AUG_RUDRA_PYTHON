#Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple = (32,45,65,98)

l = []

for i in tuple:
    l.append(i)
    if(i) == 0:
        l.remove(i)    
        t = tuple(l)
        print(tuple)