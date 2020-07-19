import cv2
trained_face_data = cv2.CascadeClassifier ("C:\\Users\\ESHU\\Desktop\\haarcascade_frontalface_default.xml")
img = cv2.imread("C:\\Users\\ESHU\\Desktop\\.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_coordinates = trained_face_data.detectMultiScale(gray_img)
#print(face_coordinates)

for (x,y,w,h) in face_coordinates:

    cv2.rectangle(img,( x,y), (x+w, y+h), (255,0,0), 10)

cv2.imshow('pxy',img)
cv2.waitKey()
print('code completed')
