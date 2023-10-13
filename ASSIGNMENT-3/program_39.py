# Write a Python function that checks whether a passed string is palindrome or not 


def isPalindrome(s):
    return s == s[::-1]
 
str1 = input("enter a word: ")
ans = isPalindrome(str1)
 
if ans:
    print("Yes")
else:
    print("No")