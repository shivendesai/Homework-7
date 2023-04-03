#Written by Shiven Desai
def caesar_cipher(s, shift):
    ciphered = ""
    for ch in s:
        if ch.isalpha():
            if ch.isupper():
                ciphered += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphered += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphered += ch
    return ciphered

string = input("Enter a message: ")
shift = int(input("Enter a shift amount: "))
ciphered_string = caesar_cipher(string, shift)
print("Ciphered message:", ciphered_string)
