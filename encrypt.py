import subprocess
from PIL import Image
import os

def clear_console():
    """Clears the console depending on the OS."""
    os.system("cls" if os.name == "nt" else "clear")

def read_text_from_file(file_path):
    """Reads text from the specified file."""
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def get_binary_data(text):
    """Converts the text to a binary string."""
    return ''.join(format(ord(char), "08b") for char in text)

def calculate_image_size(text_length):
    """
    Calculate minimum image size (width, height) 
    required to store the binary data.
    """
    side_length = int((text_length ** 0.5) + 1)
    return side_length, side_length

def create_image(width, height, background_color=(255, 0, 255)):
    """Creates a new image with the given width, height, and background color."""
    return Image.new("RGB", (width, height), background_color)

def set_pixel_color(image, x, y, color):
    """Sets a pixel color at the specified (x, y) location."""
    try:
        image.putpixel((x, y), color)
    except IndexError:
        print(f"Error at pixel: {x}, {y}")

def encode_text_in_image(image, binary_data):
    """
    Encodes binary text data into the image, setting pixel color
    to black (1) or white (0) based on each bit.
    """
    pixels = image.load()
    width, _ = image.size
    x, y = 0, 0

    for bit in binary_data:
        color = (0, 0, 0) if bit == "1" else (255, 255, 255)
        set_pixel_color(image, x, y, color)

        x += 1
        if x == width:
            x = 0
            y += 1
            if y >= image.size[1]:
                print("Warning: Text data is too long for the image size.")
                break

def save_image(image, file_name="image.png"):
    """Saves the image to the specified file."""
    try:
        image.save(file_name)
        print(f"Image saved as '{file_name}'")
    except Exception as e:
        print(f"Failed to save the image: {e}")

def main():
    clear_console()

    file_path = input("Enter the text file path: ")
    text = read_text_from_file(file_path)

    if text:
        binary_data = get_binary_data(text)
        text_length = len(binary_data)

        width, height = calculate_image_size(text_length)

        print("Binary Data: " + binary_data[:100] + "..." if len(binary_data) > 100 else binary_data)
        print(f"Binary Length: {text_length}")
        print(f"Image Dimensions: {width} x {height}")

        background_color = (255, 0, 255)  # Magenta (default)
        img = create_image(width, height, background_color)

        encode_text_in_image(img, binary_data)

        img.show()  # Display the image

        save_image(img, "encoded_image.png")

if __name__ == "__main__":
    main()
