#ATM Application
Account=100000
while True:
    
        #let think of an account user named 'Avinash' is been using a card 'c' with the pin '1234'
        #Run and observe wether different test cases of the user are working or not
        #USER INPUT
        crd=input("Enter the Card: ").lower()
        if crd=='c':
            print("$-----$-WELCOME TO ATM Mr.AVINASH-$-----$")
            pin=int(input("Enter the PIN : "))
            if pin==1234:
                print("\n Choose the Below options: \n 1.)BALANCE ENQUIRY \t \n 2.)WITHDRAWL")
                a1=int(input("Enter the sequence: "))
                if a1==1:
                    
                    #Balance Enquiry code
                    print("BALANCE ENQUIRY\n")
                    print("ACCOUNT TYPE: \n 1.)SAVINGS A/C \t \n 2.)CURRENT A/C ")
                    b1=int(input("Enter account type \t : "))
                    if b1==1:
                         print("Available Balance is : ", Account)
                    elif b1==2:
                         print(" \n U Don't have a current account pls verify \t")
                if a1==2:
                    
                    #Withdrawl code
                    print("WITHDRAWL")
                    c1=int(input("Enter withdrawl amount \t :"))
                    wdl=Account-c1
                    Account=wdl
                    print("Please take the cash")
                    print("Remaining Avail BAL : ", wdl)
                    

                
                
                
            else:
                print("\n Entered wrong pin \n")
            

                
        else:
            print("\n Entered a wrong card pls check \n")

