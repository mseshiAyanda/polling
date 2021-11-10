import cv2 as cv

img = cv.imread('photos/20160218_224545.jpg')

cv.imshow('20160218_224545.jpg', img)

cv.waitKey(0)


capture = cv.VideoCapture('videos/VID-20160218-WA0002.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
