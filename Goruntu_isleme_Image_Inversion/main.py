import numpy as np
import cv2


def resim_tersleme(resim):

    gen = resim.shape[1]
    kanallar = resim.shape[2]
    yuk = resim.shape[0]

    boyut = (yuk, gen, kanallar)

    yeni_resim = np.zeros(boyut, np.uint8)

    for x in range(0, yuk):
        for y in range(0, gen):
            for c in range(0, kanallar):
                yeni_resim[x, y, c] = 255 - resim[x, y, c]
    return yeni_resim


resim = cv2.imread("el.png")

ters_resim = resim_tersleme(resim)
cv2.imshow("orijinal",resim)

cv2.imshow("ters_resim",ters_resim)

cv2.waitKey()
cv2.destroyAllWindows()

