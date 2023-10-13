#Write a Python program to convert a tuple to a string.

n = int(input("Enter no. of entries: "))
list1 = ''



for i in range(n):
    i= input("Enter : ")
    list1 += i

string = "".join(list1)
print(string)