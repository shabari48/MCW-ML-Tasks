import os,glob
from imageoperation import ImageOperation
import cv2

class ImageProcessor:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

        
    def process_folders(self):
        folders = glob.glob(os.path.join(self.dataset_path, "img*"))
        for folder in folders:
            self.process_single_folder(folder)

    
    def process_single_folder(self, folder_path):
        
        # Read task file
        task_file = os.path.join(folder_path, "task.txt")
        with open(task_file, 'r') as f:
            tasks = f.read().splitlines()
        
        # Find images

        image_files = glob.glob(os.path.join(folder_path, "*.jpg"))

        # print(str(image_files))


        if not image_files:
            print(f"No image found in {folder_path}")
            return
            
        image_path = image_files[0]    #Take only the first image leaves out the modified images

        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to load image: {image_path}")
            return
            
        # Process image 
        
        img_op = ImageOperation(image)
        
        for task in tasks:
            task = task.strip().lower()

            if task.startswith('resize'):
                height, width = map(int, task.split()[1].split(','))
                img_op.resize(height, width)
            
            elif task.startswith('rotate'):
                angle = int(task.split()[1])
                img_op.rotate(angle)

            #Color Spaces

            elif task == 'grayscale':
                img_op.convert_grayscale()
            elif task == 'rgb':
                img_op.convert_to_rgb()

            #Blur

            elif task == 'blur':
                img_op.apply_blur()

            #Thresholding

            elif task.startswith('threshold'):
                t_value=int(task.split()[1])
                img_op.threshold(t_value)

            #Edge Detection
            elif task == 'edge':
                img_op.detect_edges()

            elif task=='contour':
                img_op.contour()

            else:
                print(f"Unknown task: {task}")

        
        # Save modified image
        base_name = os.path.basename(image_path)     #goat.jpg ->basename
        modified_name=os.path.splitext(base_name)[0]    #splitext splits it into goat[0] and jpg[1]. Take only goat

        output_path = os.path.join(folder_path, f"{modified_name}_modified.jpg")
        cv2.imwrite(output_path, img_op.image)

        
        # Creating output.txt with image information
        
    
        file_size = os.path.getsize(output_path)
        
        output_info = (
            f"File Size: {file_size} bytes\n"
            f"Dimensions: Height,Weight,Dimension {img_op.image.shape}\n"
            f"Path: {output_path}"
        )
        
        output_txt_path = os.path.join(folder_path, "output.txt")
        with open(output_txt_path, 'w') as f:
            f.write(output_info)
