import os,glob
from imageoperation import ImageOperation
import cv2

class ImageProcessor:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        
    def process_folders(self):
        """Process all folders in the dataset"""
        folders = glob.glob(os.path.join(self.dataset_path, "img*"))
        for folder in folders:
            self.process_single_folder(folder)
    
    def process_single_folder(self, folder_path):
        """Process a single folder containing an image and task file"""
        # Read task file
        task_file = os.path.join(folder_path, "task.txt")
        with open(task_file, 'r') as f:
            tasks = f.read().splitlines()
        
        # Find image file
        image_files = glob.glob(os.path.join(folder_path, "*.jpg"))
        if not image_files:
            print(f"No image found in {folder_path}")
            return
            
        image_path = image_files[0]
        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to load image: {image_path}")
            return
            
        # Process image according to tasks
        img_op = ImageOperation(image)
        
        for task in tasks:
            task = task.strip().lower()
            if task.startswith('resize'):
                img_op.resize()
            elif task.startswith('hue'):
                value = int(task.split()[1])
                img_op.adjust_hue(value)
            elif task == 'grayscale':
                img_op.convert_grayscale()
            elif task.startswith('rotate'):
                angle = int(task.split()[1])
                img_op.rotate(angle)
        
        # Save modified image
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_path = os.path.join(folder_path, f"{base_name}_modified.jpg")
        cv2.imwrite(output_path, img_op.image)
        
        # Create output.txt with image information
        height, width = img_op.image.shape[:2]
        file_size = os.path.getsize(output_path)
        
        output_info = (
            f"File Size: {file_size} bytes\n"
            f"Dimensions: {width}x{height}\n"
            f"Path: {output_path}"
        )
        
        output_txt_path = os.path.join(folder_path, "output.txt")
        with open(output_txt_path, 'w') as f:
            f.write(output_info)
