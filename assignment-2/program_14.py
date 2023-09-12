# Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string.

str1 = input("enter a string : ")
str2 = input("enter another string : ")

if len(str1) > 2 and len(str2) > 2:
    str3 = str2[:2] + str1[2:]
    str4 = str1[:2] + str2[2:]
    print(str3,end=" ")
    print(str4)
else:
    print("enter a valid string!")
