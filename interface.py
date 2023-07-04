from Bank import BankAccount
customer_dict ={} # use account no. as key and class object (customer account) as value
mobile_acc_link ={} # use mobile_nop as key and store account no. as value, for linking purpose





def new_cust():
    name = input("Enter the name of the customer")
    mobile_no =int(input('enter the number of customer: '))
    initial_depo = int(input('enter the initial deposit amount: '))
    if initial_depo <= 0:
        print('invalid amount')
        return
    pin = int(input("create Pin: "))
    customer = BankAccount(name=name,mobile_no=mobile_no,initial_depo=initial_depo,pin=pin)
    customer_dict[customer.cust_acc_num] = customer #acct. no. is stored as key and object as value
    mobile_acc_link[customer.mobile_no] = customer.cust_acc_num #mobile no. linked
    print("New user Created")
    print(f'Welcome {customer.name} to Corporate Bank. {customer.cust_acc_num} is your account number')




def login():
    account_no = int(input("Enter your account number : "))
    account_pin =int(input("Enter your Account pin: "))
    if account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin:
        print(f'\n {customer_dict[account_no].name} logged in')
        customer_dict[account_no].basic_details()
    else:
        print('Account either not exist or the pin is wrong')
        return
    while True:
        user_input1 = input("""Press 1 for deposit:
        Press 2 for withdrawl
        Press 3 for money trasfer:
        Press 4 for logout\n
        """)

        if user_input1 =="1":
            customer_dict[account_no].deposit()
        elif user_input1 == "2":
            customer_dict[account_no].withdrawl()
        elif user_input1 =="3":
            mobile = int(input("Enter the mobile number of recepient"))
            if mobile in mobile_acc_link.keys():
                secondary = mobile_acc_link[mobile] #use mobile no. to get acct no
                customer_dict[account_no].payment(customer_dict[secondary])
            else:
                print("The mobile number you have entered does not have an account assiciated with this bank")

        elif user_input1 =="4":
            print("Logged out")
            return
        else:
            print("Invalid input try again")
        print('\n#######################################\n')
        customer_dict[account_no].basic_details()






while True :
    user_input1 =input('''Press 1 for creating a new customer:
press 2 for logging in as an existing customer:
press 3 for dispaying number of customers:
press 4 for exit\n ''')
    if user_input1 == "1":
        print("Create user")
        new_cust()
    elif user_input1 =='2' :
        login()
    elif user_input1 =="3":
        print('There currently', BankAccount.no_of_cust,"customers in Corporate bank")
    elif user_input1 == '4':
        print("Exited")
        break
    else:
        print('invalidate input. Try again')
        print('\n***************************\n')
