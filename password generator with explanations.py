from cryptography.fernet import Fernet

# Function to generate and write a new key to a file (not currently used)
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

# Function to load the encryption key from a file and include the master password
def load_key(master_pwd):
    with open("key.key", "rb") as file:
        key = file.read()
    return key + master_pwd.encode()

# Function to view passwords stored in the file
def view(fer):
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(" | ")
            decrypted_pwd = fer.decrypt(passw.encode()).decode()
            print("User:", user, "| Password:", decrypted_pwd)

# Function to add a new password to the file
def add(fer):
    name = input('Account name:')
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

# Main function to control the flow of the program
def main():
    # Input master password to decrypt the key
    master_pwd = input("What is the master password? ")
    # Load encryption key with master password
    key = load_key(master_pwd)
    # Create a Fernet instance with the loaded key
    fer = Fernet(key)

    # Main loop to add/view passwords until user quits
    while True:
        # Prompt user to choose an action
        mode = input("Would you like to add a new password or view existing passwords? (add/view/q): ")
        # If user chooses to quit, break out of the loop
        if mode.lower() == "q":
            break

        # If user chooses to view passwords, call the view function
        if mode.lower() == "view":
            view(fer)
        # If user chooses to add a new password, call the add function
        elif mode.lower() == "add":
            add(fer)

# Ensures that the main function is executed only if the script is run directly
if __name__ == "__main__":
    main()
