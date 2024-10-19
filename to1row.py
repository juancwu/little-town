import cv2
import numpy as np


def spread_to_row(img, n):
    _, _, ch = img.shape
    print(ch, img.dtype)
    new_img = np.zeros((n, n * 6, ch), dtype=img.dtype)
    # copy first row to new img
    new_img[0:n, 0:n*4] = img[0:n, 0:n*4]
    new_img[0:n, n*4:n*6] = img[n:n*2, 0:n*2]
    return new_img


img = cv2.imread(
    "./little-town/assets/Resources/Trees/Tree.png", cv2.IMREAD_UNCHANGED)
new_img = spread_to_row(img, 64 * 3)
cv2.imwrite("output.png", new_img)
