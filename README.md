# CharPix

CharPix is a cross-platform Python tool designed to securely encode and decode text messages as PNG images using AES-256 encryption. It transforms any text into a base64-encrypted binary stream and visually represents it as an image. Later, it can decode and decrypt that image back into text — **only with the correct password**.

## Features

- AES-256-GCM encryption with password-based protection
- Text-to-image encoding using binary bitmaps (PNG format)
- CLI-based interface for automation and scripting
- Cross-platform compatibility (Windows, Linux, macOS)
- Zero dependencies beyond Python + Pillow + PyCryptodome
- Extensible design for future steganography or GUI features

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/QuantumByteStudios/CharPix.git
cd CharPix
pip install -r requirements.txt
```

Ensure you are using Python 3.8 or higher.

## Usage

Run the encoder or decoder from the CLI:

### Encode (Encrypt + Convert to Image)
```bash
python charpix.py encode -i message.txt -o secret.png -p yourPassword
```
- Encrypts `message.txt` using AES-256
- Converts encrypted base64 string into binary
- Outputs `secret.png`

### Decode (Image to Decrypted Text)
```bash
python charpix.py decode -i secret.png -o output.txt -p yourPassword
```
- Extracts binary data from image
- Decrypts using password
- Outputs original text to `output.txt`

## Project Structure

```
CharPix/
│
├── .gitignore                 # Git Ignore File
├── charpix.py                 # Main CLI entry point
├── LICENSE.md                 # License information
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
```

## Output

- Generates encoded PNG images (1 bit per pixel for now)
- Decryption requires exact password used during encoding
- Output text is saved to file after decoding

## Use Cases

- Share encrypted messages as images over insecure channels
- Build programming puzzles or CTF challenges
- Educate others about binary data and encryption basics
- Embed secrets in images for creative or experimental use

## Technologies

- Python 3
- Pillow (image encoding)
- PyCryptodome (AES encryption)
- Base64 encoding/decoding
- Argparse (CLI interface)

## Limitations

- Image files grow large with big inputs (currently 1-bit-per-pixel)
- Not resistant to image compression or resizing
- No embedded metadata for format validation yet
- Not a replacement for full steganography tools (yet)

## License

This project is licensed under the MIT License. See `LICENSE.md` for details.

## Author

Developed by QuantumByteStudios. Contributions and suggestions are welcome.  
For inquiries, email us at [contact@quantumbytestudios.in](mailto:contact@quantumbytestudios.in).