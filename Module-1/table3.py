a = int(input("enter number of tables between 1 to 10 :"))
if a > 10 or a<=0:
    print("error")
else:
   
    for a in range(1,a+1):
        i=int(input(f"enter number {a} to know it's table :"))
        for j in range(1,11):
            print(f"{i} * {j} = {i*j}")