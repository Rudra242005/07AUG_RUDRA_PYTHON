n = int(input("enter number of students : "))

def stdata(id,name,sub,city):
    print("ID : ",id)
    print("NAME : ",name)
    print("SUBJECT : ",sub)
    print("CITY : ",city)

for i in range(n):
    
    stid = input("Enter student ID : ")
    stnm = input("Enter student NAME : ")
    stsub = input("Enter SUBJECT : ")
    stcity = input("Enter CITY : ")
    print("\n")
    stdata(stid,stnm,stsub,stcity)
    print("\n")
