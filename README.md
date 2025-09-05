# Password Cracker 

**Password Cracker by Muakhhir** is a Python-based command-line tool designed to crack MD5, SHA1, and SHA256 hashes using a wordlist attack. The tool provides a user-friendly menu, colored output, and logs cracked passwords for easy reference.

---

## Features
- Supports **MD5**, **SHA1**, and **SHA256** hash cracking.
- Uses **wordlist attacks** for password guessing.
- **Logs cracked passwords** into `cracked.txt`.
- **User-friendly menu** interface.
- Colored CLI output using `colorama` for better visibility.
- Works with any plain-text password wordlist (`file.txt`).

---

## Installation

Run the following commands in your terminal:

git clone https://github.com/Muakhhir/Password_Cracker.git
cd Password_Cracker
pip install colorama

---

## Usage

1. Prepare a **wordlist file** named `file.txt` (one password per line) or specify the path to your own wordlist.  
2. Run the script:

python cracker.py

3. Select a hash type from the menu:  
   - `1` – SHA1  
   - `2` – MD5  
   - `3` – SHA256  
   - `4` – Quit  

4. Enter the hash you want to crack and the path to the wordlist file.  
5. If the password is found, it will display it and log it to `cracked.txt`.

---

## Example

Enter path to wordlist file (e.g., file.txt): file.txt  
Enter the SHA1 hash to crack: 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8  
[+] Password found: password  
[+] Attempts: 7  
[+] Time taken: 0.05 seconds

---

## Wordlist Example (`file.txt`)

123456  
password  
qwerty  
admin  
letmein  
welcome  
iloveyou  
monkey  
abc123  
dragon  

---

## Technologies Used
- **Python 3**
- **hashlib** (for hashing)
- **colorama** (for colored CLI output)
- **File Handling** (wordlist and log file)

---

## Author
**Muakhhir**  
GitHub: https://github.com/Muakhhir/Password_Cracker
