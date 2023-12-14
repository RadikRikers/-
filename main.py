def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted = ord(char) + shift_amount
                if shifted > ord('z'):
                    shifted -= 26
                result += chr(shifted)
            elif char.isupper():
                shifted = ord(char) + shift_amount
                if shifted > ord('Z'):
                    shifted -= 26
                result += chr(shifted)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Пример использования
message = "Hello, world!"
shift = 3
encrypted_msg = caesar_cipher_encrypt(message, shift)
print("Зашифрованное сообщение:", encrypted_msg)
decrypted_msg = caesar_cipher_decrypt(encrypted_msg, shift)
print("Расшифрованное сообщение:", decrypted_msg)
