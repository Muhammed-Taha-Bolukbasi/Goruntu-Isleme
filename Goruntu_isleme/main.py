import cv2

kamera = cv2.VideoCapture(0)

while True:

    success, goruntu = kamera.read()
    gray = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    kenar = cv2.Canny(goruntu,100,100)

    (thresh, siyah_beyaz) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


    if success:
        cv2.imshow("orijinal", goruntu)
        cv2.imshow("giri", gray)
        cv2.imshow("kenar", kenar)
        cv2.imshow('siyah-beyaz', siyah_beyaz)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
kamera.release()
cv2.destroyAllWindows()
