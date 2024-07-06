import subprocess
import os
from PIL import Image


def clear_console():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)


def read_image(file_path):
    try:
        return Image.open(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


def decode_image(image):
    pixels = image.load()
    width, height = image.size
    binary_data = ""

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            binary_data += "1" if pixel == (0, 0, 0) else "0"

    return binary_data


def binary_to_text(binary_data):
    text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        text += chr(int(byte, 2))
    return text


def main():
    clear_console()

    file_path = "image.png"
    encoded_image = read_image(file_path)

    if encoded_image is not None:
        binary_data = decode_image(encoded_image)
        decrypted_text = binary_to_text(binary_data)

        # print("Decrypted Binary: " + binary_data)
        print("Decrypted Text: " + decrypted_text)


if __name__ == "__main__":
    main()
