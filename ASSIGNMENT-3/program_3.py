"""Write a Python program to count the number of strings where the string length is 2 or more and the first and
 last character are same from a given list of strings."""

mystr = []
n = int(input("enter number of strings to enter in a string : "))
for i in range(n):
    x = input("enter strings :")
    mystr.append(x)
print(mystr)
if len(mystr)>=2:
    for i in mystr:
        if i[0]== i[-1]:
            print("the string which has same first and last character:", i)
        """else:
            pass
            #print("string has no same first and last character... ")"""
            
else:
    print("string is smaller than 2 character... ")