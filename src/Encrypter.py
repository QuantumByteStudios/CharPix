from asyncio.windows_events import NULL
import cv2 as cv
import numpy as np
import os
import platform

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

# Clear Previous Data
f = open("tempGen.txt", "a")
f.truncate(0)
f = open("tempGenO.txt", "a")
f.truncate(0)

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
cv.imshow("OUTPUT", img)

cv.waitKey(0)
cv.destroyAllWindows()
