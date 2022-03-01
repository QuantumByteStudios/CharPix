import platform
import cv2
import numpy
import os
img = cv2.imread('OUTPUT.png')

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

RGB_White = "[255255255]"
NUL = "[000]"  # BLACK
A = "[153102204]"  # AMETHYST
B = "[00255]"  # BLUE
C = "[0255255]"  # CYAN
D = "[1016733]"  # DARKBROWN
E = "[194178128]"  # EBONY
F = "[18151137]"  # FANDANGO
G = "[0171102]"  # GREEN
H = "[170152169]"  # HELIO"[TROPE204102153
I = "[113166210]"  # ICEBERG
J = "[248222126]"  # JASMINE
K = "[195176145]"  # KHAKI
L = "[214202221]"  # LAVENDER
M = "[2550255]"  # MAGENTA
N = "[233255219]"  # NYANZA
O = "[01280]"  # OCHRE
P = "[25440162]"  # PINK
Q = "[1425889]"  # QUINACRIDONE
R = "[1836514]"  # RUSTRED
S = "[24419648]"  # SAFFRON
T = "[216191216]"  # THISTLE
U = "[136120195]"  # UBE
V = "[64130109]"  # VIRIDIAN
W = "[06666]"  # WARMBLACK
X = "[115134120]"  # XANADU
Y = "[2552400]"  # YELLOWROSE
Z = "[57167142]"  # ZOMP
SPACE = "[222222222]"

WIDTH = 20
ROW = i = 0
f = open("tempGen.txt", 'a')

for inst in range(0, WIDTH):
    for i in range(0, WIDTH):
        # print(f"{ROW} + {i+1}")
        BGR = img[ROW][i]
        chk = numpy.array_str(BGR)
        f.write(chk)
        i = i + 1
    ROW = ROW + 1

f.close()

data = ""

f = open("tempGen.txt", 'r+')
fO = open("tempGenO.txt", 'r+')
for line in f:
    fO.write(line.replace(' ', ''))

f.close()
fO.close()

f2 = open("final.txt", 'r+')
fO = open("tempGenO.txt", 'r+')

checkWords = ("[255255255]", "[000]", "[153102204]", "[00255]", "[0255255]", "[1016733]", "[194178128]", "[18151137]", "[0171102]", "[170152169]", "[113166210]", "[248222126]", "[195176145]", "[214202221]",
              "[2550255]", "[233255219]", "[01280]", "[25440162]", "[1425889]", "[1836514]", "[24419648]", "[216191216]", "[136120195]", "[64130109]", "[06666]", "[115134120]", "[2552400]", "[57167142]", "[222222222]")


repWords = ("", "", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ")

for line in fO:
    for check, rep in zip(checkWords, repWords):
        line = line.replace(check, rep)
    f2.write(line)
fO.close()
f2.close()
