from __future__ import print_function
import argparse
import cv2  # PERBAIKAN: huruf kecil

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")  # PERBAIKAN: penulisan benar
args = vars(ap.parse_args())  # PERBAIKAN: function benar

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))  # PERBAIKAN: variabel r, bukan v

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))  # PERBAIKAN: variabel r, bukan v

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(0) 