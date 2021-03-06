import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('median.jpeg')

median = cv2.medianBlur(img,7)

plt.imshow(img),plt.imshow(median)

plt.show()