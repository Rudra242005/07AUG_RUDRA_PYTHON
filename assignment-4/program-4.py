#Write a Python program to read last n lines of a file.

fl=open('demo.txt','r')

n=int(input("enter number of last lines you want to read: "))

for i in (fl.readlines() [n-1:]):
   print(i)