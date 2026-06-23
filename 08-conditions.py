#Python is case sensitive hence we used string method casefold. 'a' and A are different

environment = input("Enter your environment: ")
change_ticket = False

environment = environment.casefold()

if environment == 'prod':
    print("Please provide the change ticket")

elif environment == 'staging':
    print("welcome to staging")

else:
    print("Please login using your credentials")