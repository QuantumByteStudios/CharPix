import subprocess

subprocess.call("clear", shell=True)

file = open("data.txt", "r")
data = file.read()
text = data

print("Text: " + text)

def getHexData(text):
  hexData = ""
  for i in range(len(text)):
    hexData += format(ord(text[i]), "x")
  return hexData

print("Hexadecimal: " + getHexData(text))

def getBinData(text):
  binData = ""
  for i in range(len(text)):
    binData += format(ord(text[i]), "b")
  return binData

print("Binary: " + getBinData(text))
