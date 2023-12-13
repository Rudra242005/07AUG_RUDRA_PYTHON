    #Write a Python program to write a list to a file
with open('demo.txt', 'a') as file:
    list= ['Python', 'object-oriented', 'rogramming']
    file.write(f"\n{list}\n")