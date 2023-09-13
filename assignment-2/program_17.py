"""Write a Python function that takes a list of words and returns the length
of the longest one."""

words = []

n = int(input("Enter number for word you like enter : "))

for i in range(n):
    x = input(f"enter word : ")
    words.append(x)

print(words)

def count(size):
    max = 0
    for word in size:
        word_length = len(word)
        if word_length > max:
            max = word_length
    return(max)

length = count(size = words) 
print(f"the longest word is {x} and it's length is {length}")   
