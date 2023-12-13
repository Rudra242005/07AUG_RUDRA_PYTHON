#Write a Python program to read a file line by line store it into a variable.

fl=open("demo.txt",'r')

paragraph=fl.readlines()

print(paragraph)