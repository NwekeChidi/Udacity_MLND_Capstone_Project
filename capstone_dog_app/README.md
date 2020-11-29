This flask web app accepts an image in .png, .jpeg or .jpg format, if dog(s) is detected in the image, it is classified according to its possible breed(s), if human face is detected, the closet dog breed is returned and dog filters are applied on the image.

## To test out the web app
First launch your command prompt, then set up and activate a virtual environment
__Using pip__
```
	cd Udacity_Capstone_Project/Capstone_Dog_App
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

