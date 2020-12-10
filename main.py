import cv2
import numpy as np
from time import time

def mirror(image: np.ndarray):
    result = np.array(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1] // 2):
            result[i, j] = image[i, image.shape[0] - 1 - j]
            result[i, image.shape[0] - 1 - j] = image[i, j]
    return result

def main():
    initialTime = time()
    image = cv2.imread('./image.png')
    image = mirror(image)
    print(f"Took {time() - initialTime} seconds.")

main()