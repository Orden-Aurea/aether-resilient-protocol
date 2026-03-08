import nacl.signing
import nacl.encoding

class AetherCrypto:
    @staticmethod
    def generate_keys():
        signing_key = nacl.signing.SigningKey.generate()
        verify_key = signing_key.verify_key
        return signing_key, verify_key

    @staticmethod
    def sign_message(message: str, private_key_hex: str):
        signing_key = nacl.signing.SigningKey(private_key_hex, encoder=nacl.encoding.HexEncoder)
        signed = signing_key.sign(message.encode())
        return signed.signature.hex()
