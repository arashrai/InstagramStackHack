from time import sleep, time
import cv2

img1 = cv2.imread('small_eyes_open.jpg', 0)
img2 = cv2.imread('small_eyes_closed.jpg', 0)

start = True

for _ in range(10**7):
    # ctime = time()
    cv2.imshow('image', img2)
    # print(time() - ctime)
    cv2.waitKey(1)
    # print(time() - ctime)
    cv2.imshow('image', img1)
    # print(time() - ctime)
    cv2.waitKey(900)

    if start:
        if cv2.waitKey(0) == ord('s'):
            start = False

    # print()
