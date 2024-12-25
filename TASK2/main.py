import os
from imageprocessor import ImageProcessor

def main():
    # Create instance of ImageProcessor and process all folders
    dataset=str(os.path.join(os.getcwd(),'dataset'))
    processor = ImageProcessor(dataset)
    processor.process_folders()
    print("Successfully processed images and saved them")

if __name__ == "__main__":
    main()