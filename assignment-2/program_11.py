#Write a Python program to count the number of characters (character frequency) in a string

str = input("Enter a string: ")

count = {}

for char in str:

    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for char, count in count.items():
    print(f"'{char}': {count}")

