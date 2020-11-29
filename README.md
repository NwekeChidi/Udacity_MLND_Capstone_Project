[//]: # (Image References)

[image1]: ./images/sample_dog_output.png "Sample Output"
[image2]: ./images/vgg16_model.png "VGG-16 Model Layers"
[image3]: ./images/vgg16_model_draw.png "VGG16 Model Figure"
[image4]: ./images/sample_output.png "Sample Output_1"


## Project Overview

This is the Udacity Machine Learning capstone project! In this project, I built a pipeline that can be used within a web or mobile app to process real-world, user-supplied images.  Given an image of a dog, this algorithm will identify an estimate of the canine’s breed.  If supplied an image of a human, the code will identify the resembling dog breed and apply dog filters to the image.

![Sample Output][image1]
![Sample Output_1][image4]

## Project Instructions

### Instructions

1. Clone the repository and navigate to the downloaded folder.
	
	```	
		git clone https://github.com/NwekeChidi/Udacity_MLND_Capstone_Project.git
		cd Udacity_MLND_Capstone_Project
	```
	
__NOTE:__ if you are using the Udacity workspace, you *DO NOT* need to re-download the datasets in steps 2 and 3 - they can be found in the `/data` folder as noted within the workspace Jupyter notebook.

2. Download the [dog dataset](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip).  Unzip the folder and place it in the repo, at location `path/to/dog-project/dogImages`.  The `dogImages/` folder should contain 133 folders, each corresponding to a different dog breed.
3. Download the [human dataset](http://vis-www.cs.umass.edu/lfw/lfw.tgz).  Unzip the folder and place it in the repo, at location `path/to/dog-project/lfw`.  If you are using a Windows machine, you are encouraged to use [7zip](http://www.7-zip.org/) to extract the folder. 
4. Make sure you have already installed the necessary Python packages according to the README in the program repository.
5. Open a terminal window and navigate to the project folder. Open the notebook and follow the instructions.
	
	```
		jupyter notebook dog_app.ipynb
	```

__NOTE:__ In the notebook, I trained CNNs in PyTorch which were used to classify dog breeds and detect facial keypoints.  If running the code takes too long, feel free to pursue one of the options under the section __Accelerating the Training Process__ below.



## (Optionally) Accelerating the Training Process 

If the code is taking too long to run, you will need to either reduce the complexity of your chosen CNN architecture or switch to running your code on a GPU.  If you'd like to use a GPU, you can spin up an instance of your own using AWS.

#### Amazon Web Services

You can use Amazon Web Services to launch an EC2 GPU instance. (This costs money.)

## Evaluation

The project was reviewed by a Udacity reviewer against the CNN project rubric.


## To test out the web app
First copy the model artefacts saved as "model_transfer.pt" which you created by running the cells in the notebook to the "models" folder inside the "capstone_dog_app" folder.

Launch your command prompt, then set up and activate a virtual environment

__Using pip__
```
	cd Udacity_Capstone_Project/capstone_dog_app
	py -m venv env
	pip install -r requirements.txt
	.\env\Scripts\activate
```

__Using Conda__
```
	cd Udacity_Capstone_Project/capstone_dog_app
	conda create env -f requirements_conda.yml
	conda activate env
```
After the virtual is activated, run the following commands:
```
	set FLASK_APP=dog_app.py
	set FLASK_ENV=development
	flask run
```
go to http://127.0.0.1:5000/ where the web app is ready for use.

