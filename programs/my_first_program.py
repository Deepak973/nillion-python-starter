from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    
    # Define secret inputs
    secret_message = SecretInteger(Input(name="secret_message", party=party1))
    encryption_key = SecretInteger(Input(name="encryption_key", party=party2))

    # Encryption: XOR the secret message with the encryption key
    encrypted_message = secret_message ^ encryption_key

    # Decryption: XOR the encrypted message with the encryption key to retrieve the original message
    decrypted_message = encrypted_message ^ encryption_key

    # Output the encrypted message and the decrypted message
    return [
        Output(encrypted_message, "encrypted_message", party1),
        Output(decrypted_message, "decrypted_message", party1)
    ]
