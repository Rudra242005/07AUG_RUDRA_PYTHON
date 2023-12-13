#Write a Python program to count the number of lines in a text file.

with open("demo.txt",'r') as fl:
      line= len(fl.readlines())
print(line)