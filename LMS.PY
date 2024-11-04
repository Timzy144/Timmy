import datetime
user=input()
name=input("welcome user,enter name: ")
welcomeMsg=int(input(f"welcome to iceapple library {name}\nselect 1 to proceed: "))
if welcomeMsg == 1:
    check_in=datetime.datetime.now().date()
    print(f"welcome user u checked in: ", check_in.strftime("%h-%m-%d-%y"))
    sex=input("male or female: ")
    phonenumber=int(input("please enter phone number: "))
    if check_in is True:
        print("proceed")
    
else:
    print("invalid credentials")

def Books():
    section=int(input(f"1. Section A(science)   2. Section B(psychology)\n3. Section C(sociology)\nselect options: "))
    if section==1:
        print("100 level\n200 level\n300 level\n400 level\n500 level")
    elif section==2:
        print("100 level\n200 level\n300 level\n400 level\n500 level")
    elif section==3:
        print("100 level\n200 level\n300 level\n400 level\n500 level")
    elif section==4:
        out=int(input("select 1 to proceed"))
        if out==1:
           sign_out=int(input(f"goodby {name}\nselect 1 to proceed: "))
           if sign_out == 1:
            sign_out_out=datetime.datetime.now().date()
            print(f"{name} you signed_out: ", check_in.strftime("%h-%m-%d-%y"))
        else:
         print("invalid selection")
Books()
