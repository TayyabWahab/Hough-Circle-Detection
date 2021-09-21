import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(image,caption = ''):
    plt.figure(figsize = (10,20))
    plt.title(caption)
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.show()
    
    
def circles_detect(image,dp=1,dist=1,p1=1,p2=1,minR=1,maxR=1):
    img = image.copy()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (5, 5),1)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, dist, param1 = p1,param2 = p2, minRadius = minR, maxRadius = maxR)
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        i = 0
        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 255, 0), 4)
            cv2.circle(img, (x, y), 2, (255, 0, 0), 2)
            cv2.putText(img,str(circles[i][2]),(x+5,y-5),cv2.FONT_HERSHEY_COMPLEX,0.55,(0,0,255),2)
            i = i+1
    
    display(img,'Circles')
    #cv2.imwrite('Circles.jpg',img)
    return circles
    
if __name__ == '__main__':
    image = cv2.imread('/Users/eapplestroe/Downloads/Q6_images/img1.png')
    display(image,'Original Image')
    circles = circles_detect(image,1,70,80,65,20,130)
    print('Number of Circles detected: ',len(circles))
    
