#Write a Python function to insert a string in the middle of a string.

str = ("i am  student")
sub = input("enter second string to add it in middele : ")
a = str[0:5] + sub + str[5:]
print(a)
