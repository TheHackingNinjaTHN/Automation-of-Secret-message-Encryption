import gnupg

def encrypt_message(message, pgp_key):
    gpg = gnupg.GPG()
    encrypted_data = gpg.encrypt(message, pgp_key, always_trust=True)
    return str(encrypted_data)

def main():
    message = input("Enter the message to encrypt: ")
    pgp_key = input("Enter the PGP key: ")

    encrypted_message = encrypt_message(message, pgp_key)
    print("Encrypted Message:")
    print(encrypted_message)

if __name__ == "__main__":
    main()
