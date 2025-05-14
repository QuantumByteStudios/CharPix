import argparse
import base64
import os
from math import ceil, sqrt
from PIL import Image
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

# Constants
SALT_SIZE = 16
KEY_SIZE = 32
ITERATIONS = 100_000
MAGENTA = (255, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def derive_key(password: str, salt: bytes) -> bytes:
    return PBKDF2(password, salt, dkLen=KEY_SIZE, count=ITERATIONS)


def encrypt_text(text: str, password: str) -> str:
    salt = get_random_bytes(SALT_SIZE)
    key = derive_key(password.encode(), salt)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode())
    payload = salt + cipher.nonce + tag + ciphertext
    return base64.b64encode(payload).decode()


def decrypt_text(encoded: str, password: str) -> str:
    try:
        data = base64.b64decode(encoded.encode())
        salt = data[:SALT_SIZE]
        nonce = data[SALT_SIZE:SALT_SIZE + 16]
        tag = data[SALT_SIZE + 16:SALT_SIZE + 32]
        ciphertext = data[SALT_SIZE + 32:]
        key = derive_key(password.encode(), salt)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode()
    except Exception:
        raise ValueError(
            "Decryption failed. Possibly wrong password or corrupted image.")


def text_to_binary(data: str) -> str:
    return ''.join(f"{ord(c):08b}" for c in data)


def binary_to_text(binary: str) -> str:
    chars = [chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8)]
    return ''.join(chars)


def calculate_image_size(bit_length: int) -> tuple:
    side = ceil(sqrt(bit_length))
    return side, side


def encode_to_image(binary_data: str, output_path: str):
    width, height = calculate_image_size(len(binary_data))
    img = Image.new("RGB", (width, height), MAGENTA)
    pixels = img.load()
    i = 0
    for y in range(height):
        for x in range(width):
            if i < len(binary_data):
                pixels[x, y] = BLACK if binary_data[i] == "1" else WHITE
                i += 1
    img.save(output_path)
    print(f"[+] Image saved as {output_path}")


def decode_from_image(image_path: str) -> str:
    img = Image.open(image_path)
    binary = ""
    for y in range(img.height):
        for x in range(img.width):
            binary += "1" if img.getpixel((x, y)) == BLACK else "0"
    return binary


def encode_command(args):
    if not os.path.exists(args.input):
        print("[-] Input text file not found.")
        return
    with open(args.input, 'r', encoding='utf-8') as f:
        plaintext = f.read()
    encrypted = encrypt_text(plaintext, args.password)
    binary_data = text_to_binary(encrypted)
    encode_to_image(binary_data, args.output)


def decode_command(args):
    if not os.path.exists(args.input):
        print("[-] Input image file not found.")
        return
    binary_data = decode_from_image(args.input)
    try:
        encoded_text = binary_to_text(binary_data).strip('\x00')
        decrypted_text = decrypt_text(encoded_text, args.password)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(decrypted_text)
        print(f"[+] Text successfully decoded to {args.output}")
    except Exception as e:
        print(f"[-] {str(e)}")


def main():
    parser = argparse.ArgumentParser(
        description="CharPix - Secure Text-Image Encoder/Decoder")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Encode
    encode_parser = subparsers.add_parser(
        "encode", help="Encode text into an image")
    encode_parser.add_argument(
        "--input", "-i", required=True, help="Input text file")
    encode_parser.add_argument(
        "--output", "-o", required=True, help="Output image file")
    encode_parser.add_argument(
        "--password", "-p", required=True, help="Encryption password")
    encode_parser.set_defaults(func=encode_command)

    # Decode
    decode_parser = subparsers.add_parser(
        "decode", help="Decode text from an image")
    decode_parser.add_argument(
        "--input", "-i", required=True, help="Input image file")
    decode_parser.add_argument(
        "--output", "-o", required=True, help="Output text file")
    decode_parser.add_argument(
        "--password", "-p", required=True, help="Decryption password")
    decode_parser.set_defaults(func=decode_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
