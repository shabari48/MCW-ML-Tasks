import cv2

class FilterOverlay:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        if self.image is None:
            raise ValueError(f"Could not load image: {image_path}")
        

    def apply(self, background, x, y, width, height, scale_x=1.0, scale_y=1.0):
        overlay = cv2.resize(self.image, (int(width * scale_x), int(height * scale_y)))
        h, w = overlay.shape[:2]
        
        x, y, w, h = self.adjust_boundaries(background, x, y, w, h)

        if w <= 0 or h <= 0:
            return

        if overlay.shape[2] < 4:
            overlay = cv2.cvtColor(overlay, cv2.COLOR_BGR2BGRA)

        overlay_image = overlay[:h, :w, :3]
        mask = overlay[:h, :w, 3:] / 255.0

        background_section = background[y:y+h, x:x+w]
        background[y:y+h, x:x+w] = background_section * (1-mask) + overlay_image * mask



    def adjust_boundaries(self, background, x, y, w, h):
        if x + w > background.shape[1]:
            w = background.shape[1] - x
        if y + h > background.shape[0]:
            h = background.shape[0] - y
        if x < 0:
            w += x
            x = 0
        if y < 0:
            h += y
            y = 0
        return x, y, w, h
    


    

class ImageProcessor:

    @staticmethod
    def apply_smoothing(frame,strength=0.8):
        edited = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)
        result = cv2.addWeighted(frame, 1 - strength, edited, strength, 0)
        return result
    
   
    
