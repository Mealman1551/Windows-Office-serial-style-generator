import random
import string

def generate_key():
    key_format = 'XXXXX-XXXXX-XXXXX-XXXXX-XXXXX'  # Stijl van de sleutel
    key = ''
    for char in key_format:
        if char == 'X':
            key += random.choice(string.ascii_uppercase + string.digits)
        else:
            key += char
    return key

def main():
    num_keys = 5  # Aantal sleutels om te genereren
    for _ in range(num_keys):
        serial_key = generate_key()
        print(serial_key)

if __name__ == "__main__":
    main()
input("Druk op Enter om te sluiten")