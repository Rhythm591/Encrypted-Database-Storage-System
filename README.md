# Encrypted Database Storage System

## Overview
This project demonstrates how sensitive data can be securely stored in a database using AES encryption.

User data is encrypted before being stored in SQLite and decrypted when retrieved.

## Technologies Used
- Python
- SQLite
- AES Encryption (PyCryptodome)

## Features
- Encrypt sensitive user data
- Store encrypted data in database
- Decrypt data when retrieving
- Protects confidentiality of stored data

## Security Concepts
- Data Confidentiality
- Encryption
- Secure Data Storage

## How to Run

1. Install dependencies

pip install -r requirements.txt

2. Run the program

python main.py

## Example Output

Enter Name: Rhythm
Enter Email: rhythm@gmail.com

Stored in database (encrypted):

xj28sdfkwe83...

Retrieved (decrypted):

Name: Rhythm
Email: rhythm@gmail.com
