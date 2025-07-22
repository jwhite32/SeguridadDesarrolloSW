# Importa la clase Fernet que permite realizar cifrado simétrico seguro
from cryptography.fernet import Fernet
# Genera una clave aleatoria de 32 bytes con base64 (tipo bytes). Se usará para cifrar y descifrar.
key = Fernet.generate_key()

#print(key)

# Define el mensaje original como bytes (requisito del módulo Fernet).
message = b"Encriptacion Simetrica con Python"

# Se crea un objeto Fernet que actúa como motor de cifrado, configurado con la clave generada.
engine = Fernet(key)

# Aplica el algoritmo de cifrado a message utilizando la clave cargada. El resultado es un texto cifrado ilegible.
encrypted_message =  engine.encrypt(message)

#Descifra el mensaje cifrado y muestra el texto original.
print(engine.decrypt(encrypted_message))


