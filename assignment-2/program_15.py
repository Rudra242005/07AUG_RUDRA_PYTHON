"""Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged."""

str = input("enter a string : ")
a = "ing"
b = "ly"

if len(str) >= 3:
    
    if str[-3:] == a:
        print(str + b)
    else:
        print(str + a)
else:
    print(str)