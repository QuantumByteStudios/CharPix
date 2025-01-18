import subprocess
from PIL import Image
import concurrent.futures
import time
import os


def clear_console():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)


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


def create_image(width, height, background_color):
    return Image.new("RGB", (width, height), background_color)


def set_pixel_color(image, x, y, color):
    """Sets a pixel color at the specified (x, y) location."""
    try:
        image.putpixel((x, y), color)
    except IndexError:
        print(f"Error at pixel: {x}, {y}")


def encode_text_in_image(image, text):
    width, height = image.size

    def plot_pixel(index):
        x = index % width
        y = index // width
        color = (0, 0, 0) if text[index] == "1" else (255, 255, 255)
        set_pixel_color(image, x, y, color)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(plot_pixel, range(len(text)))


def main():
    clear_console()

    file_path = input("Enter the text file path: ")
    text = read_text_from_file(file_path)

    if text is not None:
        start_time_binary = time.time()
        binary_data = get_binary_data(text)
        end_time_binary = time.time()

        text_length = len(binary_data)
        width, height = calculate_image_size(text_length)

        # print("Converting Text to Binary...")
        # print("Binary: " + binary_data)
        print('Converted text to binary successfully.')
        print("Text Length (Binary): " + str(text_length))
        print("Image: (Width: " + str(width) + " Height: " + str(height) + ")")

        background_color = (255, 0, 255)  # Magenta
        img = create_image(width, height, background_color)

        start_time_plotting = time.time()
        encode_text_in_image(img, binary_data)
        end_time_plotting = time.time()

        print(f"Time taken to convert text to binary: {
              end_time_binary - start_time_binary:.6f} seconds")
        print(f"Time taken to plot image: {
              end_time_plotting - start_time_plotting:.6f} seconds")

        img.show()
        img.save("image.png")


if __name__ == "__main__":
    main()
