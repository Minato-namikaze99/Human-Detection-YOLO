# Human-Detection-YOLO
This is a model that I made which detects the humans in an Image, and then returns the count of humans in the picture as well as makes a boundary to point out the humans in the image. 

I would personally recommend you to make a virtual environment as there are libraries which can result in conflicts with the libraries present on your device. Although I never faced this issue in my device.
If you don't want to create a virtual environment, skip to the next section.

### Creating a virtual environment
At first, locate to the folder you cloned the repository into.

#### Installing the virtualenv Library
Launch a Command Line Interpreter in that address and run the following command:
```
$ pip install virtualenv
```
> Do remember that pip must be in your environment variables.
> NOTE - Don't worry, if you have already installed the library, it will just show "Requirements already satisfied".

#### Creating a virtual environment
Then, write the following command:

```
$ virtualenv my_name
```
> Replace the "my_name" with the name of the folder that you want to give to the virtual environment.

Then, change the directory using this command:

```
$ cd my_name
```
> Change "my_name" to the name of the virtual environment that you have mentioned before.

#### Activating the virtual environment
You can initiate the Virtual Environment now by just writing the following command:
```
$ Scripts\activate
```

The Virtual Environment has been succesfully created and has started running.

#### Deactivating the virtual environment 
You can easily deactivate the virtual environment by using this command:
```
$ deactivate
```

### Cloning the repository
Now, you can easily clone the repository either by using GitHub Desktop, or by typing the command:
```
$ git clone <the ssh or the https link to the repository>
```

### Installing Libraries
After successful cloning, we need to install the libraries so that the Flask App runs smoothly.

Run the following commands, one by one:
```
$ pip install flask

$ pip install opencv-python

$ pip install Pillow

$ pip install ultralytics==8.0.9

$ git clone https://github.com/ultralytics/ultralytics

$ pip install -qe ultralytics
```

Now, you are all set to run the Flask App. 

### Running the flask app
By default, the flask app executes in the IP address "http://127.0.0.1:5000/objectdetection/".

## References
I referred to the following links while creating this model, 
    1. https://www.youtube.com/watch?v=8SQcB2g_cp4
    2. https://python.plainenglish.io/develop-your-machine-learning-api-for-image-object-detection-yolov8-with-python-flask-api-f393cb7e1e43