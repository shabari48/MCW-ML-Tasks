# McW Tasks Project

This repository contains Python and ML tasks I completed as part of the McW tasks project. The tasks were designed to test my understanding of Python

## TASK1: Car Class Implementation

A simple car class hierarchy implementation demonstrating object-oriented programming concepts in Python.

### Files Structure
- `car.py`: Base car class implementation
- `ev.py`: Electric vehicle class implementation
- `gascar.py`: Gas vehicle class implementation
- `main.py`: Main driver code demonstrating the usage

### Class Hierarchy
- `Car`: Base class with common car properties
  - `ElectricVehicle`: Inherits from Car, specific to electric vehicles
  - `GasVehicle`: Inherits from Car, specific to gas-powered vehicles

## TASK2: Image Processing System

An automated image processing system that applies various transformations to images based on task specifications provided in text files.

### Files Structure
```
TASK2/
├── dataset/
│   ├── img1/
│   │   ├── task.txt
│   │   └── [image files]
│   ├── img2/
│   │   ├── task.txt
│   │   └── [image files]
│   └── ...
├── imageoperation.py
├── imageprocessor.py
└── main.py
```

### Features
- Processes multiple image folders automatically
- Supports various image operations:
  - Resize
  - Hue adjustment
  - Grayscale conversion
  - Image rotation
- Generates output files with processed image information
- Creates modified images with transformation applied

### Supported Operations
1. `Resize`: Scales the image to 50% of original size
2. `Hue <value>`: Adjusts the hue by specified value
3. `Grayscale`: Converts image to grayscale
4. `Rotate <angle>`: Rotates image by specified angle

### Output
For each processed image, the system generates:
- A modified image with suffix '_modified'
- An output.txt file containing:
  - File size
  - Image dimensions
  - File path

## Requirements
- Python 3.x
- OpenCV (cv2)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/shabari48/MCW-ML-Tasks.git
```

2. Install required packages:
```bash
pip install opencv-python 
```

## Usage

### TASK1
```bash
cd TASK1
python main.py
```

### TASK2
1. Place your images in separate folders under the dataset directory
2. Create a task.txt file in each image folder with desired operations
3. Run the processing script:
```bash
cd TASK2
python main.py
```

## Task File Format
Each task.txt file should contain one operation per line. Example:
```
Resize
Hue 30
Grayscale
Rotate 45
```

## License
[MIT License](https://opensource.org/licenses/MIT)