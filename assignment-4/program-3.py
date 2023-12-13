#Write a Python program to read first n lines of a file.
fl=open('demo.txt','r')

n=int(input("enter number of lines you want to read: "))

for i in (fl.readlines() [0:n]):
   print(i)

