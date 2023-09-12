name = input("enter student's name : ")
rollno = int(input("enter student's roll no. : "))

s1 = int(input("enter marks of subject 1 : "))
s2 = int(input("enter marks of subject 2 : "))
s3 = int(input("enter marks of subject 3 : "))
s4 = int(input("enter marks of subject 4 : "))
if s1< 33 or s2< 33 or s3< 33 or s4 < 33:
    print("fail")
else:
    print(f"student's name is {name}")
    print(f"student's roll no. is {rollno}")
    total = s1+s2+s3+s4
    print(f"your total is {total}")

    per = total/4
    print(f"you scored {per}%")

    if per > 90:
        print("distinction")
    elif per > 70:
        print("first class")
    elif per > 50:
        print("second class")
    elif per > 33:
        print("pass class")
    else:
        print("fail")