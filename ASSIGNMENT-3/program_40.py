#Write a Python program to read a random line from a file.

import random

print(random.choice(open("stud.txt","r").readline().split()))