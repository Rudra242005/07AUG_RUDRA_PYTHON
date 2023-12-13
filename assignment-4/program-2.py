#Write a Python program to append text to a file and display the text.

fl=open('data.txt','a')

stid=input("Enter ID:")
stnm=input("Enter Name:")


fl.write(f"ID:{stid}\nName:{stnm}\n--------------\n")

fl=open('data.txt','r')

print(fl.read())