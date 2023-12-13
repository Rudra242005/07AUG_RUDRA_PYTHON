#Write a Python program to read a file line by line and store it into a list

fl=open("demo.txt",'r')
list = [fl.readlines()]
for i in list:
    print(i)
