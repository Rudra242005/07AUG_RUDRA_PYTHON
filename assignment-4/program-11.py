#Write a Python program to copy the contents of a file to another file.
fl=open("demo.txt",'r')
cpy=fl.read()

fl2 = open("new.txt",'a')
fl2.write(cpy)