# This is my Password-Generator
by Reha Demircan
Password Manager with Encryption This project is a simple password manager that allows you to store and retrieve passwords securely using encryption. The program utilizes the cryptography.fernet module to encrypt passwords before saving them and decrypt them when retrieved.
Features
Password Storage: Store passwords for different accounts securely.
Password Retrieval: View decrypted passwords for stored accounts.
Master Password Protection: The stored passwords are encrypted and can only be accessed with the correct master password.
How It Works
Master Password: The user provides a master password that is used to unlock the encryption key.
Encryption: Passwords are encrypted using the Fernet symmetric encryption from the cryptography library.
Storage: Encrypted passwords are stored in a text file (password.txt).
Decryption: The encrypted passwords can be decrypted only with the correct master password.
Prerequisites
Python 3.x
cryptography module (pip install cryptography)
File Structure
key.key: This file contains the encryption key used to encrypt and decrypt passwords.
password.txt: This file stores the encrypted passwords in the format Account Name | Encrypted Password.
How to Use
1. Running the Program
Run the script:
bash
Kodu kopyala
python password_manager.py
2. Master Password
When prompted, enter your master password. This password will be used to unlock the encryption key.
3. Adding a New Password
Choose add to add a new password.
Enter the account name and password. The password will be encrypted and saved in the password.txt file.
4. Viewing Stored Passwords
Choose view to see stored passwords. The program will decrypt the stored passwords and display them in plain text.
5. Quit
Choose q to quit the program.
Example
sql
Kodu kopyala
What is the master password? ********
Would you like to add a new password or view existing passwords? (add/view/q): add
Account name: GitHub
Password: mySecurePassword123

Would you like to add a new password or view existing passwords? (add/view/q): view
User: GitHub | Password: mySecurePassword123

Would you like to add a new password or view existing passwords? (add/view/q): q
Important Notes
The encryption key must be generated and stored securely.
Keep your master password safe; without it, the stored passwords cannot be decrypted.
The password.txt file stores sensitive data (even though encrypted), so be careful not to share it or expose it to unauthorized access.
