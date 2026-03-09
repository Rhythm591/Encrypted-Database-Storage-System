from encryption import encrypt_data, decrypt_data
from database import create_table, insert_data, get_all_data

def add_user():
    name = input("Enter Name: ")
    email = input("Enter Email: ")

    encrypted_name = encrypt_data(name)
    encrypted_email = encrypt_data(email)

    insert_data(encrypted_name, encrypted_email)

    print("Data encrypted and stored successfully!\n")


def view_users():
    users = get_all_data()

    print("\nStored Users (Decrypted):")

    for user in users:
        id = user[0]
        name = decrypt_data(user[1])
        email = decrypt_data(user[2])

        print(f"ID: {id} | Name: {name} | Email: {email}")


def main():
    create_table()

    while True:
        print("\nEncrypted Database Storage System")
        print("1. Add User")
        print("2. View Users")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_user()

        elif choice == "2":
            view_users()

        elif choice == "3":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
