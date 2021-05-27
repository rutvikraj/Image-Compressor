# Compresso - An Intelligent Image Compressor

Compresso compresses an image by detecting the important and unimportant objects inside a frame and compressing them accordingly. In short, YOLO is used to detect and segment the objects and then the compression is done respectively. 

### Requirements
1. Python 3.6
2. OpenCV
3. PyTorch 0.4
4. Numpy

*Using PyTorch 0.3 will break the detector.


1. Clone, and `cd` into the repo directory. 
   ```Shell
   git clone https://github.com/zeeem/EndPresso.git
   cd EndPresso
   ```
2. Install the required dependencies if necessary:
   
   - Python 3
   - Install Pytorch following [THIS LINK](https://pytorch.org/get-started/locally/)
   - Other python dependencies: PIL (Pillow version), numpy, openCV

*Also in the project there is "requirements.txt" file which contains all the project requirements. Now to install at of these requirenments at once you can use `pip install -r requirements.txt`.


## How to run the application

### Running the EndPresso commandline app

`cd` to the prject directory and run the app by the following command in the terminal.

```
python detect.py --images images/test3.jpg --quality 10
```

Here,

`--images` flag defines the directory to load images from, 
`--quality` is an optional flag. Its the rate of the compression where 0 = highest compression (lowest quality) and 100 = lowest compression(highest quality). As default it's 10.
`images/test3.jpg` is the source image. Change it accordingly. 

The output file will be saved in the `output` directory with the filename `res.jpg`.

### Running the EndPresso GUI app

- So the basic GUI home screen looks like this when you execute the "ep_gui.py" file as shown in below image.

![Homescreen](https://github.com/rutvikraj/Image-Compressor/blob/main/gui_images/main_screen.png)

- As you can see on home sceen there are two Buttons one to Select the image and another to Compress the image. Also when you start the GUI no image is selected so it shows a message "No !mage Selected".

![Buttons](https://github.com/rutvikraj/Image-Compressor/blob/main/gui_images/Buttons.png)

- Here are some Screenshots of what will happen when you click on those buttons.
   - Clicking on rleft button it will open explorer for you to select Image.
   - ![Button !](https://github.com/rutvikraj/Image-Compressor/blob/main/gui_images/B1_pressed.png)
   - On clicking to the right button after selecting an Image it in background start its process of compressing & after the process is completed you will get either of the one message box.
   -  ![Notification](https://github.com/rutvikraj/Image-Compressor/blob/main/gui_images/notifi.png) - ![Notification](https://github.com/rutvikraj/Image-Compressor/blob/main/gui_images/notify.png)
   - If your image is compressed succesfully the you will get the first notification from above as shown with Compression Ratio and also the output ditrctory where your compessed image is saved as shown below.
   - ![Notification](https://github.com/rutvikraj/Image-Compressor/blob/main/gui_images/uotput.png) 
   - But if you get the other notification then you need to change the image because it cannot be compressed.
   - The output file will be saved in the `output` directory with the filename `res.jpg`.



## Compression Results

![Result Comparison](https://github.com/zeeem/EndPresso/blob/master/temp/res_comparison.png)

![Compression Information](https://github.com/zeeem/EndPresso/blob/master/temp/res_compression_info.png)



## Developers
[Naimur Rahman Jeem](https://www.linkedin.com/in/zeeem/)

[Hanming Li](https://www.linkedin.com/in/hanming-li-306b11199/)

## Acknowledgements
The code is based on the official code of [YOLO v3](https://github.com/pjreddie/darknet), PyTorch part of the original code, by [marvis](https://github.com/marvis/pytorch-yolo2), as well as PyTorch implementation of the YOLO v3 by [ayooshkathuria](https://github.com/ayooshkathuria/pytorch-yolo-v3)

The weights file "yolov3.weights" is downloaded from [here](https://pjreddie.com/media/files/yolov3.weights)


If needed, please contact at rahmanje[at]ualberta[dot]ca, hanming[at]ualberta[dot]ca.
