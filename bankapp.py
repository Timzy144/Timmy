bank=100000
def pin():
    pin=int(input("Enter your pin: "))
    if pin==1234:
      return True
    else:
      print("invalid input")


def dashboard():
    print(f'1. withdraw   2. deposit\n3. checkbalance   4. transfer\n5. changepin   6. quickteller\n7. Home ')
    dash=int(input("select options: "))
    if dash==1:
        withdraw=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\n5. other\nselect amoount: '))
        if withdraw==1:
         print(f"${500} withdraw successful")    
        elif withdraw==2:
         print(f"${1000} withdraw successful")
        elif withdraw==3:
         print(f"${1500} withdraw successful")
        elif withdraw==4:
         print(f"${2000} withdraw successful") 
        elif withdraw==5:
           otheramount=int(input("Enter amount: "))
           if otheramount==2500:
              print(f"${2500} successful")
           else:
               print("invalid input") 
        else:
           print("invalid selection")
           
    

    if dash==2:
       deposit=int(input(f'1. iceapple bank   2. other\nselect bank: '))
       if deposit==1:
          print(f"welcome\nenter account number: ")
       elif deposit==2:
          print(f"1. gt bank   2. opay\n3. palm pay   4. polaris bank: ")  
          otherbank=int(input(f"select bank: ")) 
          if otherbank==1:
             print(f"welcome\nenter account number: ") 
          elif otherbank==2:
             print(f"welcome\nenter account number")
          elif otherbank==3:
             print(f"welcome\nenter account number")
          elif otherbank==4:
             print(f"welcome\nenter account number")         
          
       else:
        print("invalid input")

        
    

    if dash==3:
       pin()
       checkbalance=int(input(f'1. iceapple bank   2. other\nselect bank: '))
       if checkbalance==1:
          print("welcome\nplease enter your account number")
       elif checkbalance==2:
         print(f"1. gt bank   2. opay\n3. palm pay   4. polaris bank: ")
         othercheck=int(input(f"select bank: "))
         if othercheck==1:
            print("welcome to gt bank\nplease enter your account number")
         elif othercheck==2:
            print("welcome to opay\nplease enter your account number")
         elif othercheck==3:
            print("welcome to palm pay\nplease enter your account number")
         elif othercheck==4:
            print("welcome to polaris bank \nplease enter your account number")
         else:
           print("invalid selection")
         
    

    if dash==4:
      transfer=int(input(f"1. iceapple bank\n Timmy Jeje\n 000xxxxxxxx11\n 2. Ahmad bank\n Bello\n 111xxxxxxxx22\n 3. palmpay\n 704xxxxx25\n Paul\n4. other\nselect options: "))
      if transfer==1:
         beneficiary=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nselect amount: '))
         if beneficiary==1:
          print(f"${500}transfer successful")
         elif beneficiary==2:
            print(f"${1000}transfer successful")
         elif beneficiary==3:
            print(f"${1500}transfer successful")
         elif beneficiary==4:
            print(f"${2000}transfer successful")
         else:
            print("invalid selection")
            
      elif transfer==2:
         if beneficiary==1:
          print(f"${500}transfer successful")
         elif beneficiary==2:
            print(f"${1000}transfer successful")
         elif beneficiary==3:
            print(f"${1500}transfer successful")
         elif beneficiary==4:
            print(f"${2000}transfer successful")
         else:
            print("invalid selection")
            
      elif transfer==3:
         if beneficiary==1:
          print(f"${500} transfer successful")
         elif beneficiary==2:
            print(f"${1000} transfer successful")
         elif beneficiary==3:
            print(f"${1500} transfer successful")
         elif beneficiary==4:
            print(f"${2000} transfer successful")
         else:
            print("invalid selection")
                
      elif transfer==4:
         othertransfer=int(input(f"1. gt bank   2. opay\n3. polaris bank:\nselect bank: "))         
         if othertransfer==1:
            print("Enter account number")
         elif othertransfer==2:
            print("Enter account number")   
         elif othertransfer==3:
            print("Enter account number")
         else:
            print("invalid selection")
      else:
         print("invalid selection")
         
                
    if dash==5:
      pin()
      changepin=int(input('Enter new pin: ')) 
      if changepin==12345:
         confirmpin=int(input('Confirm new pin: '))
         if confirmpin ==changepin:
            print("change of pin successful")
      else:
         print("invalid input")            
         

    elif dash==6:
      quickteller=int(input('1. Pay Electrical bill  2. Airtime recharge\n3. Data top-up\nselect options: '))
      if quickteller==1:
            electricalbill=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nselect amount: '))
            if electricalbill==1:
               print(f"${500} successful")
            elif electricalbill==2:
               print(f"${1000} successful")
            elif electricalbill==3:
               print(f"${1500} successful")
            elif electricalbill==4:
               print(f"${2000} successful")
            else:
               print("invalid selection")
      else:
         print("invalid selection")            
            
      if quickteller==2:
         airtime=int(input(f'1. MTN   2. AIRTEL\n3. GLO   4. Other\nSelect network: '))
         if airtime==1:
            MTN=int(input('Enter phone number: '))
            if MTN==11111111111:
             mtn=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nSelect amount:'))
             if mtn==1:
                  print(f"${500} Airtime subscription successful")
             if mtn==2:
                  print(f"${1000} Airtime subscription successful")
             if mtn==3:
                  print(f"${1500} Airtime subscription successfull")
             if mtn==4:
               print(f"${2000} Airtime subscription successful")
             else:
               print("invalid selection")
         else:
            print("invalid selection")
            

      elif airtime==2:
         AIRTEL=int(input('Enter phone number: '))
         if AIRTEL==00000000000:
          airtel=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nSelect amount:'))
          if airtel==1:
               print(f"${500} Airtime subscription successful")
          if airtel==2:
               print(f"${1000} Airtime subscription successful")
          if airtel==3:
               print(f"${1500} Airtime subscription successful")
          if airtel==4:
               print(f"${2000} Airtime subscription successful")
          else:
            print("invalid selection")
         else:
          print("invalid selection")
         

      if airtime==3:
         GLO=int(input('Enter phone number: '))
         if GLO==22222222222:
           glo=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nSelect amount:'))
           if glo==1:
                  print(f"${500} Airtime subscription successful")
           if glo==2:
                  print(f"${1000} Airtime subscription successful")
           if glo==3:
                  print(f"${1500} Airtime subscription successful")
           if glo==4:
                  print(f"${2000} Airtime subscription successful")
           else:
               print("invalid selection")
      else:
            print("invalid selection")
                    

      if airtime==4:
         othernet=int(input(f'1. 9mobile 2. Ntel'))
         if othernet==1:
            othernetamt9=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nselect amount: '))
            if othernetamt9==1:
                  print(f'${500} Airtime subscription successful')
            if othernetamt9==2:
                  print(f"${1000} Airtime subscription successful") 
            if othernetamt9==3:
                  print(f"${1500} Airtime subscription successful")
            if othernetamt9==4:
                  print(f"${2000} Airtime subscription successful")
            else:
                  print("invalid selection")
         else:
               print("invalid selection")      
               
         if othernet==2:
            othernetamtN=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nselect amount: '))
            if othernetamtN==1:
                  print(f"${500} Airtime subscription successful") 
            if othernetamtN==2:
                  print(f"${1000} Airtime subscription successful")  
            if othernetamtN==3:
                  print(f"${1500} Airtime subscription successful") 
            if othernetamtN==4:
                  print(f"${2000} Airtime subscription successful")
            else:
                  print("invalid selection")
         else:
               print("invalid selection")
               
      if quickteller==3:
         data=int(input(f'1. MTN   2. AIRTEL\n3. GLO   4. Other\nSelect network: '))
         if data==1:
            MTNdata=int(input('Enter phone number: '))
            if MTNdata==11111111111:
               mtndata=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nSelect amount:'))
               if mtndata==1:
                   print(f"${500} Data  subscription successful")
               if mtndata==2:
                   print(f"${1000} Data  subscription successful")
               if mtndata==3:
                   print(f"${1500} AData  subscription successfull")
               if mtndata==4:
                   print(f"${2000} Data  subscription successful")
               else:
                   print("invalid selection")
            else:
                print("invalid selection")
                
         elif data==2:
            AIRTELdata=int(input('Enter phone number: '))
            if AIRTELdata==22222222222:
               airteldata=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nSelect amount:'))
               if airteldata==1:
                  print(f"${500} Data  subscription successful")
               if airteldata==2:
                  print(f"${1000} Data  subscription successful")
               if airteldata==3:
                  print(f"${1500} Data  subscription successful")
               if airteldata==4:
                  print(f"${2000} Data  subscription successful")
               else:
                  print("invalid selection")
            else:
               print("invalid selection")
         else:
            print("invalid selection")      
               

      elif data==3:
            GLOdata=int(input('Enter phone number: '))
            glodata=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nSelect amount:'))
            if glodata==1:
                  print(f"${500} Data  subscription successful")
            if glodata==2:
                  print(f"${1000} Data  subscription successful")
            if glodata==3:
                  print(f"${1500} Data  subscription successful")
            if glodata==4:
                  print(f"${2000} Data  subscription successful")
            else:
                  print("invalid selection")
      else:
               print("invalid selection")   
               

      if data==4:
         othernetdata=int(input(f'1. 9mobile 2. Ntel\nselect options: '))
         if othernetdata==1:
            othernetamtdata9=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nselect amount: '))
            if othernetamtdata9==1:
                  print(f'${500} Data  subscription successful')
            if othernetamtdata9==2:
                  print(f"${1000} Data  subscription successful") 
            if othernetamtdata9==3:
                  print(f"${1500} Data  subscription successful")
            if othernetamtdata9==4:
                  print(f"${2000} Data subscription successful")
            else:
                  print("invalid selection")  
      else:
         print("invalid selection")             
         
      if othernet==2:
         othernetamtdataN=int(input(f'1. $500   2. $1000\n3. $1500   4. $2000\nselect amount: '))
         if othernetamtdataN==1:
                  print(f"${500} Data subscription successful") 
         if othernetamtdataN==2:
                  print(f"${1000} Data subscription successful")  
         if othernetamtdataN==3:
                  print(f"${1500} Data subscription successful") 
         if othernetamtdataN==4:
                  print(f"${2000} Data subscription successful")
         else:
                  print("invalid selection")
                  return home()
      else:
               print("invalid selection")
    else:
      print("invalid input")

def home():
     home=int(input("Enter 0 to go back: "))
     if home==0:
       dashboard()
     else:
         print("invalid input/selection")   
     


    
pin()
dashboard()
home()
