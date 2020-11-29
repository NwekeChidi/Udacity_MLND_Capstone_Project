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


