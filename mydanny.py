import cv2

img = cv2.imread('Data/danny.jpg')

while True:
    cv2.imshow('Danny', img)
    
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()