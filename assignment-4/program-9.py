#Write a Python program to count the frequency of words in a file.

with open("demo.txt",'r')as file:
    line= file.read()

word = input("Enter the word to check it's freq: ")
result = line.count(word)
print(f"Number of substring {word}:", result)
