
keys=['id','name','sub']

r = int(input("enter number of student's data:"))
for i in range(r):
    stdata={}
    for j in range(len(keys)):
        v = input(f"enter value of {keys[j]}:")
        stdata[keys[j]]=v
   
    print(stdata)