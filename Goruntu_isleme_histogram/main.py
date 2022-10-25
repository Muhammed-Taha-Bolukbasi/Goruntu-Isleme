import cv2
import numpy as np
from matplotlib import pyplot as plt

foto = cv2.imread("pa.jpg")
cv2.imshow("kus", foto)

B = foto[:, :, 0]  # mavi
G = foto[:, :, 1]  # yesil
R = foto[:, :, 2]  # kirmizi

cv2.imshow("mavi", B)
cv2.imshow("yesil", G)
cv2.imshow("kirmizi", R)

cv2.waitKey()



print(foto.shape)   # yoğunluk yazdırma
print(R.shape)

x = 0
y = 0
kanal = 0

yogunluk_rgb = foto[y, x, kanal]
print("yog= ", yogunluk_rgb)

yogunluk_r = R[y, x]
print("yog_gray= ", yogunluk_r)

yogunluk_g = G[y, x]
print("yog_gray2= ", yogunluk_g)

yogunluk_b = B[y, x]
print("yog_gray3= ", yogunluk_b)

max_yogunluk = np.max(B)
print("max yog= ", max_yogunluk)

min_yogunluk = np.min(B)
print("min yog= ", min_yogunluk)

# tam koordinatın rgb degerlerini donderme

print(foto[y, x])

# parça piksel alma
parca = R[20:30, 40:50]
print("par= ", parca)

renkli = cv2.imread("pa.jpg")
gri = cv2.imread("pa.jpg", 0)

cv2.imshow("gri", gri)
histColor = cv2.calcHist(renkli, [0], None, [256], [0, 256])
histGray = cv2.calcHist(gri, [0], None, [256], [0, 256])

plt.figure(2, facecolor="purple")
plt.plot(histGray)

B = renkli[:, :, 0]
hist_B = cv2.calcHist([B], [0], None, [256], [0, 256])
print("numpy")
print(np.sum(hist_B))  # satir ve sutunlari topluyor(mus)

plt.figure(3, facecolor="purple")
plt.hist(gri.ravel(), 256, [0, 256])
plt.show()
