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
2. `Hue`: Adjusts the hue by specified value
3. `Grayscale`: Converts image to grayscale
4. `Rotate`: Rotates image by specified angle

### Output
For each processed image, the system generates:
- A modified image with suffix '_modified'
- An output.txt file containing:
  - File size
  - Image dimensions
  - File path

## TASK3: Real-time Face Filter Application

A real-time face filter application using OpenCV for face detection and filter application. The application allows users to apply various filters (glasses, hats, animal faces) to detected faces in the webcam feed.

### Files Structure
```
TASK3/
├── images/
│   ├── glasses.png
│   ├── hat.png
│   └── animal.png
|
|__ sounds/
│   ├── glasses.png
│   ├── hat.png
│   └── animal.png
└── main.py
```

### Features
- Real-time face detection using OpenCV's Haar Cascade Classifier
- Multiple filter options:
  - Glasses filter
  - Hat filter
  - Animal face filter
- Command-line interface for filter selection
- Automatic camera detection
- Sound effects for filter application

### Supported Filters
1. Glasses (-g): Overlays glasses on detected faces
2. Hat (-t): Places a hat above detected faces
3. Animal (-a): Applies animal face filter over detected faces

### Command Line Arguments
- `-g` or `--glasses`: Apply glasses filter
- `-t` or `--hat`: Apply hat filter
- `-a` or `--animal`: Apply animal filter


### Usage Examples
```bash
# Apply glasses filter
python main.py -g

# Apply hat filter
python main.py -t

# Apply animal filter
python main.py -a


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
pip install tkinter
pip install ttkbootstrap
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

### TASK3
1. Ensure your webcam is connected and accessible
2. Place filter images in the filters directory
3. Run the application with desired filters:
```bash
cd TASK3
python main.py -g / -t / -a
```

## Task File Format (TASK2)
Each task.txt file should contain one operation per line. Example:
```
Resize
Hue 30
Grayscale
Rotate 45
```

## License
[MIT License](https://opensource.org/licenses/MIT)