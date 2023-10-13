#Write a Python function to get the largest number, smallest num and sum of all from a list.

numbers =[]
n = int(input("enter a number : "))

for i in range(n):
    x = int(input("enter numbers : "))
    numbers.append(x)
print(numbers)
print("The largest number in the list is:",max(numbers))
print("The smallest number in the list is:",min(numbers))
print("The sume of list elements is:",sum(numbers))