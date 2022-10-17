import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

foto = cv2.imread("pa.jpg")
cv2.imshow("papagan",foto)


B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]

cv2.imshow("Mavi",B)
cv2.imshow("Yesil",G)
cv2.imshow("Kirmizi",R)

imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(imgGray, cmap='gray')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()