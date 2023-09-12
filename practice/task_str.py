fnm = input("enter your first name : ")
lnm = input("enter your last name : ")

if fnm.isupper() and lnm.isupper():
    print("move to next step.")
    em = input("enter your E-MAIL : ")
    if em.islower():
        print("GREAT! move to next step.")
        pws = input("enter your password : ")
        rpws = input("reenter password : ")
        if pws == rpws and rpws.isalnum:
            print("looks good! moving to last step ")
            pn = (input("enter your phone number : "))
            if pn.isdigit():
                print("your data has been submitted!")
            else:
                print("oops something went wrong please kindly check your data and enter appropriate data!")
        else:
            print("oops something went wrong please kindly check your data and enter appropriate data!")
    else:
        print("oops something went wrong please kindly check your data and enter appropriate data!")
else:
    print("oops something went wrong please kindly check your data and enter appropriate data!")

