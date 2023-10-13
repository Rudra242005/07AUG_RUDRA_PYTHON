# Write a Python program to create a dictionary from a string.

Sample_string= 'w3resource' 


my_dict = {}

for i in Sample_string:
    my_dict[i] = my_dict.get(i, 0) + 1
print(my_dict)