import subprocess
import os
from PIL import Image
import time


def clear_console():
    """Clears the console depending on the OS."""
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For Linux and MacOS
        os.system("clear")


def read_image(file_path):
    """Reads an image from the specified file path."""
    try:
        return Image.open(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error opening image: {e}")
        return None


def decode_image(image):
    """
    Decodes binary data from the image, interpreting black pixels (0,0,0)
    as '1' and white pixels (255,255,255) as '0'.
    """
    pixels = image.load()
    width, height = image.size
    binary_data = ""

    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            # If pixel is black, consider it as '1', otherwise '0'
            binary_data += "1" if pixel == (0, 0, 0) else "0"

    return binary_data


def binary_to_text(binary_data):
    """
    Converts a binary string into readable text, interpreting 8 bits (1 byte)
    at a time.
    """
    text = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:  # Only process full bytes
            text += chr(int(byte, 2))
    return text


def main():
    clear_console()

    file_path = input("Enter the image file path to decode: ")
    encoded_image = read_image(file_path)

    if encoded_image is not None:
        start_time_decoding = time.time()
        binary_data = decode_image(encoded_image)
        end_time_decoding = time.time()

        start_time_text_conversion = time.time()
        decrypted_text = binary_to_text(binary_data)
        end_time_text_conversion = time.time()

        print(f"Time taken to decode image: {
              end_time_decoding - start_time_decoding:.6f} seconds")
        print(f"Time taken to convert binary to text: {
              end_time_text_conversion - start_time_text_conversion:.6f} seconds")
        print("Decrypted Text: " + decrypted_text)


if __name__ == "__main__":
    main()
