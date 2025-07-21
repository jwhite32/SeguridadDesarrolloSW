from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

message = b"Encriptacion Simetrica con Python"

engine = Fernet(key)

encrypted_message =  engine.encrypt(message)

print(engine.decrypt(encrypted_message))


