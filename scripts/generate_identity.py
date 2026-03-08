import nacl.signing
import nacl.encoding

# Generar llave privada
signing_key = nacl.signing.SigningKey.generate()
# Obtener llave pública (la que compartirías)
verify_key = signing_key.verify_key

print("-" * 30)
print("🔑 TU IDENTIDAD AETHER GENERADA")
print("-" * 30)
print(f"LLAVE PRIVADA (HEX): {signing_key.encode(encoder=nacl.encoding.HexEncoder).decode()}")
print(f"LLAVE PÚBLICA (HEX): {verify_key.encode(encoder=nacl.encoding.HexEncoder).decode()}")
print("-" * 30)
print("⚠️ GUARDA LA PRIVADA EN UN LUGAR SEGURO. NO LA COMPARTAS.")