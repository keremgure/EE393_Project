# EE393_Project
EE393(Python for Enginners) Class Term Project
> *Authors: **Kerem Güre**, **Cenker Karaörs**  
**Ertuğrul Özvardar**, **Doğukan Duduoğlu***  
> *Desc: This project uses the TensorFlow Object Detection API and utilizes the webcam to detect the objects seen by the camera.*  
> *Date: 28/12/2019*

## Installation
1. Download and install Python 3.6.x (**Make sure it is 3.6! Very Important!!**)
2. Make sure Python installation is in the PATH (For windows users)
3. Clone the repo.
4. Download the tensorflow repo from [here](https://github.com/tensorflow/models).
5. put the `object_detection` folder(inside the tensorflow repo you downloaded), to the root of this repo's clone directory.
6. Update `pip` and `setuptools` by running
    ```sh
    python -m pip install --upgrade pip setuptools
    ```
7. cd into the cloned folder.
8. Install required libraries by running
    ```sh
        python -m pip install -r requirements.txt
    ```
9. run the program via
    ```sh
    python detectionGui.py
    ```
    The first time the program is run, It will download all the neccecary model files and cache them for next usages.
10. Enjoy!
---
## Usage

The program by default uses `ssd_mobilenet_v1_coco_2017_11_17` model for object detection. This can be changed by updating the `model_to_use` variable inside `detectionGui.py`, by one of the models defined [here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md).

---
## Explanation

1. The program utilizes the `threading` library to smoothen the GUI experience whilst loading the model since it can take a while for it to load.

2. Inside `detectionGui.py` there is `notification` function that can spawn non-blocking tkinter Toplevel widgets to show various messages.

3. Some helper functions are used to initilize threading such as, `camera_helper` and `load_helper`.
4. _callback functions are called when pressed for each of the buttons in the GUI.

5. `tensor_run` file implements all the functionality required for the `TensorFlow Object Detection API`.
    
         For detailed explanation please see the comments in the code.
6. Various commandline print statements are placed around the code for easy understanding of what part of the GUI does what.