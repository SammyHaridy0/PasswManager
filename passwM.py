import getpass

passwordData = {}

def choose_password():
    website = input("What website is this for?\n")
    username = input("What is the username?\n")
    password = getpass.getpass("Type in a password\n")  
    passwordStorage(website, username, password)
    print(f"Your username '{username}' has the password set for {website}.\n")

def passwordStorage(userWebsite, userUsername, userPassword):
    if userWebsite not in passwordData:
        passwordData[userWebsite] = {}
    if userUsername in passwordData[userWebsite]:
        print("Warning: Username already exists for this website. No action taken.")
    else:
        passwordData[userWebsite][userUsername] = userPassword

def main():
    print("Welcome to the password set up.\n")
    while True:
        choose_password()
        keepgoing = input("Do you want to add another password? (yes/no): ").lower()
        
        if keepgoing == 'no':
            break

    print(f"\nHere is your stored data: {passwordData}")
    for website, credentials in passwordData.items():
        for username in credentials:
            print(f"Website: {website}\nUsername: {username}\nPassword: {'*' * len(credentials[username])}\n")





if __name__ == "__main__":
    main()









    
    
