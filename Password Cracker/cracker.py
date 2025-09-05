import hashlib
import time
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def crack_hash(hash_to_crack, algorithm, wordlist_file):
    """Try to crack a hash using a wordlist and specified algorithm."""
    try:
        with open(wordlist_file, "r", encoding="utf-8") as file:
            start_time = time.time()
            for count, guess in enumerate(file, 1):
                guess = guess.strip()
                if algorithm == "md5":
                    hashedGuess = hashlib.md5(guess.encode()).hexdigest()
                elif algorithm == "sha1":
                    hashedGuess = hashlib.sha1(guess.encode()).hexdigest()
                elif algorithm == "sha256":
                    hashedGuess = hashlib.sha256(guess.encode()).hexdigest()
                else:
                    print(Fore.RED + "Unsupported algorithm!")
                    return False

                if hashedGuess.upper() == hash_to_crack.upper():
                    end_time = time.time()
                    print(Fore.GREEN + f"\n[+] Password found: {guess}")
                    print(Fore.CYAN + f"[+] Attempts: {count}")
                    print(Fore.CYAN + f"[+] Time taken: {end_time - start_time:.2f} seconds")

                    # Save to cracked.txt
                    with open("cracked.txt", "a") as log:
                        log.write(f"{algorithm.upper()} | {hash_to_crack} -> {guess}\n")
                    return True

                if count % 500 == 0:
                    print(Fore.YELLOW + f"[*] Tried {count} passwords so far...")

            print(Fore.RED + "[-] Password not found in wordlist.")
            return False

    except FileNotFoundError:
        print(Fore.RED + f"Wordlist file '{wordlist_file}' not found!")
        return False


def main():
    # Banner
    print(Fore.GREEN + Style.BRIGHT)
    print(r"""
  ____                                  _   _                 
 |  _ \ __ _ ___ _____      _____  __ _| | | |__   __ _  ___  
 | |_) / _` / __/ __\ \ /\ / / _ \/ _` | | | '_ \ / _` |/ _ \ 
 |  __/ (_| \__ \__ \\ V  V /  __/ (_| | | | | | | (_| |  __/ 
 |_|   \__,_|___/___/ \_/\_/ \___|\__,_| |_| |_|\__, |\___|  
                                               |___/         
             PASSWORD CRACKER BY MUAKHHIR
""")
    print("=" * 60 + "\n")

    while True:
        print("Select an option:")
        print("1. SHA1 Hash")
        print("2. MD5 Hash")
        print("3. SHA256 Hash")
        print("4. Quit Script\n")
        choice = input("> ")

        if choice in ["1", "2", "3"]:
            hash_type = {"1": "sha1", "2": "md5", "3": "sha256"}[choice]
            target_hash = input(Fore.CYAN + f"Enter the {hash_type.upper()} hash to crack:\n> ").strip()
            wordlist = input(Fore.CYAN + "Enter path to wordlist file (e.g., file.txt): ").strip()
            crack_hash(target_hash, hash_type, wordlist)

        elif choice == "4":
            print(Fore.CYAN + "Exiting... Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
