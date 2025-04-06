from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key  

# Uncomment the following line to create the key file the first time you run the script
# write_key()

try:
    master_pwd = input("What is your master password? ")
    key = load_key() + master_pwd.encode()
    fer = Fernet(key)

    def add():
        name = input("Account Name: ")
        pwd = input("Password: ")
        with open("password.txt", "a") as f:
            f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

    def view():
        with open("password.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                try:
                    print("User:", user, "; Password:", fer.decrypt(passw.encode()).decode())
                except Exception as e:
                    print(f"Failed to decrypt password for {user}: {e}")

    while True:
        mode = input("Would you like to add a new password or view existing ones? (add/view), press q to quit: ").lower()
        if mode == "q":
            break
        elif mode == "add":
            add()
        elif mode == "view":
            view()
        else:
            print("Invalid mode! Please choose 'add' or 'view'.")

except Exception as e:
    print(f"An error occurred: {e}. Please check your key or reset your data.")


