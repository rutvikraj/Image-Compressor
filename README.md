# Compresso - An Intelligent Image Compressor

Compresso compresses an image by detecting the important and unimportant objects inside a frame and compressing them accordingly. In short, YOLO is used to detect and segment the objects and then the compression is done respectively. 

## Installation

### Requirements
1. Python 3.6
2. OpenCV
3. PyTorch 0.4
4. Numpy

*Using PyTorch 0.3 will break the detector.


1. Clone, and `cd` into the repo directory. 
   ```Shell
   git clone https://github.com/Chailcy/compresso.git
   cd Compresso
   ```
2. Install the required dependencies if necessary:
   
   - Python 3
   - Install Pytorch following [THIS LINK](https://pytorch.org/get-started/locally/)
   - Other python dependencies: PIL (Pillow version), numpy, openCV



## How to run the application

### Running the Compresso commandline app

The app is still in alpha so there is no GUI developed yet.
`cd` to the prject directory and run the app by the following command in the terminal.

```
python detect.py --images images/test3.jpg --quality 10
```

Here,

`--images` flag defines the directory to load images from, 
`--quality` is an optional flag. Its the rate of the compression where 0 = highest compression (lowest quality) and 100 = lowest compression(highest quality). As default it's 10.
`images/test3.jpg` is the source image. Change it accordingly. 

The output file will be saved in the `output` directory with the filename `res.jpg`.


## Acknowledgements
The code is based on the official code of [YOLO v3](https://github.com/pjreddie/darknet), PyTorch part of the original code, by [marvis](https://github.com/marvis/pytorch-yolo2), as well as PyTorch implementation of the YOLO v3 by [ayooshkathuria](https://github.com/ayooshkathuria/pytorch-yolo-v3)

The weights file "yolov3.weights" is downloaded from [here](https://pjreddie.com/media/files/yolov3.weights)
