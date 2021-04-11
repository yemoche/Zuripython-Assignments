def moneyWithdrawal():
    print("withdrawal")

def moneyDeposited():
    print('Money deposited')
    bankModeOfOperations()
#login function
def login():
    print('******login into your new account*****')

    accountNumber = int(input("enter your account number" '\n'))
    password = input('enter your password \n')   

    for accountNumber,password in customersDatabase.items():
        bankModeOfOperations()        
    print('invalid account or password')
    

def bankModeOfOperations():
     #print('Welcome %s ' % ()
     selectedOption = int(input('what would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n'))


     if (selectedOption == 1):
            moneyDeposited()
     elif (selectedOption == 2):
            moneyWithdrawal()
     elif (selectedOption == 3):
            logout()
     elif (selectedOption == 4): 
            exit()
     else:
            print('invalid option selected')
            bankModeOfOperations()

    #Logout function
def  logout():
      login()
   
#using Dictionary key pair values to capture customers database
import random
customersDatabase = {}

#Account number generation for all customers

def accountNumberGeneration():
    return random.randrange(111111111,999999999)

#Registration of new customers
def registrationOfNewCustomers():
    firstName = input("Enter your First Name:\n")
    lastName = input("Enter your Last Name:\n")
    emailAddress = input("Enter your email address:\n")
    password = input("Enter your password:\n")
    accountNumber= accountNumberGeneration()
    castName = '{} {}'.format(firstName, lastName)

    #generating a database storage of customers records using a dictionary key pair values method
    customersDatabase[accountNumber] = [ firstName, lastName, emailAddress, password]

    print('Your account has been created')
    print("==========================")
    print('You are welcome, Mr %s' % castName )
    print("Your new account number is %d"% (accountNumberGeneration()))
    print("Keep your account number safe")
    print("==============================")
    
    login()


#Welcome page
def welcomePage():
    print("You are welcome to Capitol Bank")
    accountConfirmer = int(input("do you have an acccount with us: 1(Yes) 2(No)" '\n'))
    if (accountConfirmer == 1):
        login()
    elif (accountConfirmer == 2):
        registrationOfNewCustomers()
    else: 
        print("You need to enter a valid input to bank with us")
    welcomePage()
welcomePage()
