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

### Usage

```bash
cd TASK1
python main.py
```

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


### Usage
1. Place your images in separate folders under the dataset directory
2. Create a task.txt file in each image folder with desired operations
3. Run the processing script:
```bash
cd TASK2
python main.py
```

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


### Usage
1. Ensure your webcam is connected and accessible
2. Place filter images in the filters directory
3. Run the application with desired filters:
```bash
cd TASK3
python main.py -g / -t / -a
```

### Task File Format (TASK2)
Each task.txt file should contain one operation per line. Example:
```
Resize
Hue 30
Grayscale
Rotate 45
```

## TASK 4 Exploratory Data Analyis on Zomato Dataset



An exploratory data analysis (EDA) project on the Zomato dataset to uncover insights and trends in the restaurant industry.

### Dataset
The dataset can be downloaded from [Kaggle](https://www.kaggle.com/datasets/rishikeshkonapure/zomato).

### Files Structure
```
TASK4/
├── dataset/
│   └── zomato.csv
├── zomato.ipynb

```

### Features
- Data cleaning and preprocessing
- Descriptive statistics and data visualization
- Analysis of restaurant ratings, cuisines, and locations
- Insights on price range and customer reviews

### Usage
1. Download the dataset from Kaggle and place it in the `dataset` directory.
2. Install the required packages:
```bash
pip install numpy pandas matplotlib seaborn wordcloud
```
3. Open the Jupyter notebook and run the cells to perform the analysis:
```bash
jupyter notebook zomato.ipynb
```

## TASK5  Implementatoin of Machine Learning Library from Scratch - ShaSha
### About ShaSha Library

ShaSha is a custom machine learning library developed from scratch using NumPy. It provides essential machine learning algorithms and utilities for data preprocessing, model training, and evaluation. The library is designed to be simple, efficient, and easy to use for educational purposes and small-scale projects.

### Features
- Linear Regression
- Multivariate Linear Regression
- Logistic Regression
- Decision Trees
- Random Forest
- K-Nearest Neighbors (KNN)


### Datasets Used for Testing
The ShaSha library has been tested on various datasets to ensure its robustness and accuracy:
- [Red Wine Quality](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)
- [Bank Marketing](https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing)
- [Salary Dataset (Simple Linear Regression)](https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression)
- [Insurance](https://www.kaggle.com/datasets/mirichoi0218/insurance)

### Repository
The source code and documentation for the ShaSha library can be found in the [GitHub repository](https://github.com/shabari48/shasha).

### Installation
To install the ShaSha library and install the required packages:
```bash
pip install shahsa numpy
```


### Usage

> **Note:** Always normalize and standardize your data before feeding it into the model. Ensure that the input data is in the form of a NumPy array .

Import the library and use the provided classes and functions to build and evaluate machine learning models:
```python
import shasha


# Example: Linear Regression
from shasha import My_Linear_Regression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```
