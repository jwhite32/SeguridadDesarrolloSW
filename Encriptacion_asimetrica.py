"""
Script de Encriptación Asimétrica en Python utilizando la librería 'cryptography'.
Este ejemplo usa RSA para generar claves, cifrar y descifrar un mensaje.
Cada bloque de código incluye comentarios explicativos.
"""

# Importación de librerías necesarias
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# =======================
# 1. Generar la clave privada RSA
# =======================
private_key = rsa.generate_private_key(
    public_exponent=65537,     # Valor estándar seguro del exponente público
    key_size=2048,             # Longitud de la clave (más bits = más seguridad)
    backend=default_backend()  # Motor criptográfico por defecto
)

# =======================
# 2. Obtener la clave pública desde la clave privada
# =======================
public_key = private_key.public_key()

# =======================
# 3. Serializar y guardar la clave privada en un archivo PEM
# =======================
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,  # Formato estándar de clave privada
    encryption_algorithm=serialization.NoEncryption()  # Sin cifrado (solo para pruebas)
)

with open("private_key.pem", "wb") as f:
    f.write(pem_private)

# =======================
# 4. Serializar y guardar la clave pública en un archivo PEM
# =======================
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo  # Formato estándar de clave pública
)

with open("public_key.pem", "wb") as f:
    f.write(pem_public)

# =======================
# 5. Leer las claves desde los archivos
# =======================
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,
        backend=default_backend()
    )

with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )

# =======================
# 6. Cifrar un mensaje con la clave pública
# =======================
message = input("Insert message: ").encode()  # Convierte el texto ingresado en bytes

encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Función de relleno OAEP con SHA-256
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nMensaje cifrado (bytes):\n", encrypted_message)

# =======================
# 7. Descifrar el mensaje con la clave privada
# =======================
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("\nMensaje descifrado:\n", decrypted_message.decode())  # Decodifica los bytes a texto
