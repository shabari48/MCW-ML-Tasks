import cv2 
import numpy as np

class ImageOperation:
    def __init__(self, image):
        self.image = image
    
    def resize(self, height,width):
        #image.shape returns (height, width, channels)
        #but resize takes (width, height)
        self.image = cv2.resize(self.image, (width, height))
        return self.image

    def rotate(self, angle):
        
        height, width = self.image.shape[:2]
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        self.image = cv2.warpAffine(self.image, rotation_matrix, (width, height))
        # self.image=cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
    
    #Colour Spaces

    def convert_to_rgb(self):
        self.image=cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
       
    
    def convert_grayscale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        
    
    #Apply blur

    def apply_blur(self):
        self.image = cv2.GaussianBlur(self.image,(7,7),0)
        # self.image = cv2.medianBlur(self.image,7)
        
    
    #Thresholding

    def threshold(self,t_value):
        self.convert_grayscale()
        # _,self.image = cv2.threshold(self.image,t_value,255,cv2.THRESH_BINARY)
        self.image = cv2.adaptiveThreshold(self.image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
        
    
    #Edge Detection

    def detect_edges(self):
        self.image=cv2.erode(self.image,np.ones((2,2),np.uint8))
        self.image=cv2.Canny(self.image,150,250)
        # self.image=cv2.dilate(self.image,np.ones((2,2),np.uint8),iterations=2)
        

    def contour(self):
        
        self.convert_grayscale()
       
        _, thresh = cv2.threshold(self.image, 80, 255, cv2.THRESH_BINARY_INV)
       
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 100:  
                
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 0, 255), 2)