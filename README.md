[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/) 

# Predictive_speech
You are giving a speech and get stuck, do not worry I have a solution for you. This project uses **raspberry pi** and a usb **microphone** to record your speech continuously. I have used the **speech_recognition** library in python to listen to that speech, decode it continuously to text using **google recognizer** and disply it with the help of a **pygame** window. After speaking a minimum number of words it shows the dialog box in the same window with a prediction of what you might have said next. The prediction is done using a **LSTM** model with work from Charles Dickens as dataset.

**IBM-Watson** - Since this is a pure IoT project, IBM cloud computing resources are used to deploy the model and predict output accordingly.

THe only backside of this prject seems to be the bare minimum lag caused by compilation of various working functions.


### Prerequisites

What things you need to install the software and how to install them

```
pickle
numpy
keras
speech_recognition
pygame
watson_machine_learning_client
os
contextlib
```

## Getting Started

Download a python interpeter preferable a version beyond 3.0. Install the prerequisute libraries given above.Cross-check variable directories and train the model with few changes here and there. Then deploy the model to IBM. Run compile.py file to start giving a speech without fear and see the prediction in a pygame window.

```
$train.py

$deploy.py

$compile.py     

```

## Output
[![Watch the video](https://github.com/Shaashwat05/Predictive_speech/blob/master/output.png)](https://github.com/Shaashwat05/Predictive_speech/blob/master/output.mp4)


## Built With

* [python](https://www.python.org/) - The software used
## Author
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Profile-teal.svg)](https://www.linkedin.com/in/shaashwat-agrawal-1904a117a/)

* [**Shaashwat Agrawal**](https://github.com/Shaashwat05)


## Documentation

The whole documentation and explanation of code as well as concepts can be found in this article : https://iot4beginners.com/predictive-speech-with-raspberry-pi-and-deep-learning/

