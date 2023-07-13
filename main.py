import subprocess
from PIL import Image

subprocess.call("cls", shell=True)

file = open("file.txt", "r")
data = file.read()
text = data

# print("Text: " + text)

def getHexData(text):
  hexData = ""
  for i in range(len(text)):
    hexData += format(ord(text[i]), "x")
  return hexData

# print("Hexadecimal: " + getHexData(text))

def getBinData(text):
  binData = ""
  for i in range(len(text)):
    binData += format(ord(text[i]), "b")
  return binData

text = getBinData(text)
textLength = len(text)

def calculateImageSize(textLength):
  width = 0
  height = 0
  while width * height < textLength: 
    width += 1
    height += 1
  return width, height

width, height = calculateImageSize(textLength)

print("Binary: " + text)
print("Length: " + str(textLength))
print("Width: " + str(width) + " Height: " + str(height))

# Image Processing
img = Image.new("RGB", (width, height), "white")

pixels = img.load()

imageWidth = img.size[0]

# Write pixels
# pixels[X, Y] = (R, G, B)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

x = 0 # X coordinate
y = 0 # Y coordinate

for i in range(len(text)):
  # print("X: " + str(x) + " Y: " + str(y))
  if text[i] == "1":
    try:
      pixels[x, y] = BLACK
    except:
      print("Error at pixel, c(B): " + str(x) + " " + str(y))
      break
  else:
    try:
      pixels[x, y] = WHITE
    except:
      print("Error at pixel c(W): " + str(x) + " " + str(y))
      break

  x += 1 # Move to the right
  if x == imageWidth: # If the end of the line is reached
    x = 0 # Move to the left
    y += 1 # Move down

img.show()
img.save("image.png")