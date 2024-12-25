import cv2

class ImageOperation:
    def __init__(self, image):
        self.image = image
    
    def resize(self, scale=0.5):
        """Resize image by scale factor"""
        width = int(self.image.shape[1] * scale)
        height = int(self.image.shape[0] * scale)
        self.image = cv2.resize(self.image, (width, height))
        return self.image
    
    def adjust_hue(self, value):
        """Adjust hue of the image"""
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        hsv[:,:,0] = (hsv[:,:,0] + value) % 180
        self.image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        return self.image
    
    def convert_grayscale(self):
        """Convert image to grayscale"""
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return self.image
    
    def rotate(self, angle):
        """Rotate image by specified angle"""
        height, width = self.image.shape[:2]
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        self.image = cv2.warpAffine(self.image, rotation_matrix, (width, height))
        return self.image