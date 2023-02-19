from asyncio.windows_events import NULL
import cv2 as cv
import numpy as np
import utils as session

session.clear()

# Clear Previous Data
f = open("tempGen.txt", "a", encoding="utf_8")
f.truncate(0)
f.close()
f = open("tempGenO.txt", "a", encoding="utf_8")
f.truncate(0)
f.close()

RGB_White = (255, 255, 255)
NUL = (0, 0, 0)      # BLACK
A = (153, 102, 204)  # AMETHYST
B = (0, 0, 255)      # BLUE
C = (0, 255, 255)    # CYAN
D = (101, 67, 33)    # DARK BROWN
E = (194, 178, 128)  # EBONY
F = (181, 51, 137)   # FANDANGO
G = (0, 171, 102)    # GREEN
H = (170, 152, 169)  # HELIO(TROPE 204 102 153
I = (113, 166, 210)  # ICEBERG
J = (248, 222, 126)  # JASMINE
K = (195, 176, 145)  # KHAKI
L = (214, 202, 221)  # LAVENDER
M = (255, 0, 255)    # MAGENTA
N = (233, 255, 219)  # NYANZA
O = (0, 128, 0)      # OCHRE
P = (254, 40, 162)   # PINK
Q = (142, 58, 89)    # QUINACRIDONE
R = (183, 65, 14)    # RUST RED
S = (244, 196, 48)   # SAFFRON
T = (216, 191, 216)  # THISTLE
U = (136, 120, 195)  # UBE
V = (64, 130, 109)   # VIRIDIAN
W = (0, 66, 66)      # WARM BLACK
X = (115, 134, 120)  # XANADU
Y = (255, 240, 0)    # YELLOW ROSE
Z = (57, 167, 142)   # ZOMP
SPACE = (222, 222, 222)

STRING = input("Enter Your Message: ")
STRING = STRING.upper()

# Default Values For Now
WIDTH = 10
HEIGHT = 10

img = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)

ROW = i = 0

for inst in range(0, len(STRING)):
    ALPHA = STRING[inst]
    # print(f"{ROW} + {i}")
    if i == WIDTH:
        ROW = ROW + 1
        i = 0
    else:
        if ALPHA == "A":
            cv.rectangle(img, (i, ROW), (i, ROW), A, -1)
        elif ALPHA == "B":
            cv.rectangle(img, (i, ROW), (i, ROW), B, -1)
        elif ALPHA == "C":
            cv.rectangle(img, (i, ROW), (i, ROW), C, -1)
        elif ALPHA == "D":
            cv.rectangle(img, (i, ROW), (i, ROW), D, -1)
        elif ALPHA == "E":
            cv.rectangle(img, (i, ROW), (i, ROW), E, -1)
        elif ALPHA == "F":
            cv.rectangle(img, (i, ROW), (i, ROW), F, -1)
        elif ALPHA == "G":
            cv.rectangle(img, (i, ROW), (i, ROW), G, -1)
        elif ALPHA == "H":
            cv.rectangle(img, (i, ROW), (i, ROW), H, -1)
        elif ALPHA == "I":
            cv.rectangle(img, (i, ROW), (i, ROW), I, -1)
        elif ALPHA == "J":
            cv.rectangle(img, (i, ROW), (i, ROW), J, -1)
        elif ALPHA == "K":
            cv.rectangle(img, (i, ROW), (i, ROW), K, -1)
        elif ALPHA == "L":
            cv.rectangle(img, (i, ROW), (i, ROW), L, -1)
        elif ALPHA == "M":
            cv.rectangle(img, (i, ROW), (i, ROW), M, -1)
        elif ALPHA == "N":
            cv.rectangle(img, (i, ROW), (i, ROW), N, -1)
        elif ALPHA == "O":
            cv.rectangle(img, (i, ROW), (i, ROW), O, -1)
        elif ALPHA == "P":
            cv.rectangle(img, (i, ROW), (i, ROW), P, -1)
        elif ALPHA == "Q":
            cv.rectangle(img, (i, ROW), (i, ROW), Q, -1)
        elif ALPHA == "R":
            cv.rectangle(img, (i, ROW), (i, ROW), R, -1)
        elif ALPHA == "S":
            cv.rectangle(img, (i, ROW), (i, ROW), S, -1)
        elif ALPHA == "T":
            cv.rectangle(img, (i, ROW), (i, ROW), T, -1)
        elif ALPHA == "U":
            cv.rectangle(img, (i, ROW), (i, ROW), U, -1)
        elif ALPHA == "V":
            cv.rectangle(img, (i, ROW), (i, ROW), V, -1)
        elif ALPHA == "W":
            cv.rectangle(img, (i, ROW), (i, ROW), W, -1)
        elif ALPHA == "X":
            cv.rectangle(img, (i, ROW), (i, ROW), X, -1)
        elif ALPHA == "Y":
            cv.rectangle(img, (i, ROW), (i, ROW), Y, -1)
        elif ALPHA == "Z":
            cv.rectangle(img, (i, ROW), (i, ROW), Z, -1)
        elif ALPHA == " ":
            cv.rectangle(img, (i, ROW), (i, ROW), SPACE, -1)
        else:
            cv.rectangle(img, (i, ROW), (i, ROW), NULL, -1)
        i = i+1

cv.imwrite("OUTPUT.png", img)
cv.imshow("OUTPUT.png", img)

cv.waitKey(0)
cv.destroyAllWindows()
