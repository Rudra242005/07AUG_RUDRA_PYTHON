#Write a Python function to reverses a string if its length is a multiple of 4.

str = input("enter a string : ")

def mystr(getdata):
    
   if len(getdata) % 4 ==0:
      return getdata[::-1]
   else:
      return getdata
   
x = mystr(getdata = str)
print(x)    

