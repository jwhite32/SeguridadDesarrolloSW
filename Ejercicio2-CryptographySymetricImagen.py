# Importación de Fernet desde la librería cryptography
from cryptography.fernet import Fernet

#Lectura de la clave secreta (key) desde el archivo my_secret.txt
with open("my_secret.txt", "r") as secrets_file:
    key = secrets_file.readline()

#Se crea el motor de cifrado engine usando la clave leída.
engine = Fernet(key)

#Se abre y se lee la imagen original chelsea.png en modo binario (rb).
with open("chelsea.png", "rb") as original_image:
    original_image_as_bytes = original_image.read()

# Cifrado de la imagen original
encrypted_image = engine.encrypt(original_image_as_bytes)
with open("encrypted_image.png", "wb") as encrypted_image_dest:
      encrypted_image_dest.write(encrypted_image)

# Descifrado de la imagen:
with open("encrypted_image.png", "rb") as encrypted_image_input:
    encrypted_image = encrypted_image_input.read()
    decrypted_image = engine.decrypt(encrypted_image)
    with open("decrypted_image_fine.png", "wb") as decrypted_image_dest:
         decrypted_image_dest.write(decrypted_image)