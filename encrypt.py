import subprocess
from PIL import Image

def clear_console():
    subprocess.call("cls", shell=True)

def read_text_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def get_binary_data(text):
    return ''.join(format(ord(char), "08b") for char in text)

def calculate_image_size(text_length):
    side_length = int(text_length ** 0.5) + 1
    return side_length, side_length

def create_image(width, height, background_color):
    return Image.new("RGB", (width, height), background_color)

def set_pixel_color(image, x, y, color):
    try:
        image.putpixel((x, y), color)
    except IndexError:
        print(f"Error at pixel: {x}, {y}")

def encode_text_in_image(image, text):
    pixels = image.load()
    width, _ = image.size
    x, y = 0, 0

    for bit in text:
        color = (0, 0, 0) if bit == "1" else (255, 255, 255)
        set_pixel_color(image, x, y, color)

        x += 1
        if x == width:
            x = 0
            y += 1

def main():
    clear_console()

    file_path = "data.txt"
    text = read_text_from_file(file_path)

    if text is not None:
        binary_data = get_binary_data(text)
        text_length = len(binary_data)

        width, height = calculate_image_size(text_length)

        print("Binary: " + binary_data)
        print("Length: " + str(text_length))
        print("Width: " + str(width) + " Height: " + str(height))

        background_color = (255, 0, 255)  # Magenta
        img = create_image(width, height, background_color)

        encode_text_in_image(img, binary_data)

        img.show()
        img.save("image.png")

if __name__ == "__main__":
    main()
