# Books-Info-App #

A rudimentary “full-stack” django app that allows users to view books available and their info.

Visit: http://karthic.pythonanywhere.com/

## Dependencies for Project: ##

1. Python 2.7
2. Django 1.11+
3. Django REST framework
4. Bootstrap - already provided through CDN in project file (however you can install it or modify as you need.)
5. jQuery - already provided through CDN in project file
6. SQLite - as the database (already pre-installed with the project on django)

## APIs Used: ##

1. Google Books API

## Instructions on how to install and run the project: ##

Visit the site at http://karthic.pythonanywhere.com/ to explore the application.

1. Make sure Python 2 (version 2.7) is installed; in Command Prompt or PowerShell, type ```python --version```  (else install Python and ensure the Python path is updated in Environment Variables)
	- To install Python - (Windows)
		1. Download from https://www.python.org/downloads/
		2. Be sure to check you're downloading the right python version for your system (64bit vs 32bit) 
		3. Open Python Installer - Customize as per requirements and change install Location and use: `C:\Python27
		4. Click ```Install```
		5. Update the Python path in Environment Variables of the system
		6. Verify installation - in Command Prompt or PowerShell, type ```python --v``` or ```python -version```
	- If Python is installed correctly, we use pip to install other components and packages
2. Make sure you have django installed (else install django 1.11.X)
	- To install django - (Windows)
		1. Open Command Prompt or PowerShell (Run as adminstrator)
		2. Type ```pip install django==1.11.3```
			*NOTE: django==1.11.3 is for version 1.11.3. If you need a different version, replace those numbers accordingly. Such as django==1.8.7 or django==1.10.7 or django==1.11.2. This is true for any python package.
	- It is highly recommended that you install and run django on a **Virtual Environment**; to do this open Command Prompt or PowerShell
		1. Type ```pip install virtualenv```
		2. Navigate to your project directory and make virtualenv parent directory 
			- ```mkdir 'homedirname'```
			- ```cd 'homedirname'```
		3. Create virtualenv by typing ```virtualenv .``` or ```virtualenv yourenvname```
		4. Go to your virtual environment directory ```cd yourenvname```
		5. Activate your environment:
			- ```cd \path\to\your\virtualen\env\ ```
 			- ```cd ~\dirname\homedirname```
 			- ```.\Scripts\activate```
		6. To Reactivate and Deactivate Virtualenv
			- ```cd ~\dirname\homedirname # or your virtualenv's path```
			- ```.\Scripts\activate```
			-```(homedirname) > deactivate```
			- ```.\Scripts\activate```
			- ```(homedirname) >```
		7. Now install django or any Python Package as mention in the above point		
3. Install Django REST framework using command ```pip install djangorestframework```
       - To provide REST services and API endpoints
4. Now clone or download the github repo to the correct directory
5. Go ```cd``` to the cloned or downloaded project directory where you will see a manage.py file
6. Now we need to create and migrate the database Models
	- In the cmd type and run ```python manage.py migrate tasklistapp```
	- Then run ```python manage.py makemigration tasklistapp```
	- Next, ```python manage.py sqlmigrate tasklistapp 0001```
	- Finally, run ```python manage.py migrate```
7. We need to create a Superuser (Administrator) for the django admin panel who can control all aspects of the app and authentication/authorization
	- Type ```python manage.py createsuperuser```
	- Enter the appropriate details - (username and password to login to the admin panel)
8. To get our localhost running, django provides us with a simple server to test and run apps
	- Type ```python manage.py runserver```
	- This should start running our ```http://localhost:8000``` at http://127.0.0.1:8000 - (Defaults to port 8000)
9. Now, visit http://127.0.0.1:8000/admin and login to access your database models, groups and users
10. Create necessary groups and users as per requirements - auth for people who can access and use our app
	- Ensure normal users only have ```Active``` permissions check, not admin or superuser status
11. **Start** using the app by just visitng the localhost or ```http://127.0.0.1:8000/```
	- Auth for different users vary
12. Still adding a lot of features and ironing out a few small bugs - ** The App works properly for the provided features **



## The following are the API (JSON) endpoints: ##

1. http://127.0.0.1:8000/api/ (at /api)

2. http://127.0.0.1:8000/api/books/ (at /api/books)


** Still adding more API (JSON) endpoints which filters results according to specific requests. ** Basic endpoints work.

## Comments and Notes: ##
1. Just done with front-end view mockup. Need to add a lot of back-end functionality and refine front-end design.

2. Still working on a few features:
	- [ ] Ability to add, delete and modify book data
	- [ ] Need to add **ARIA** attributes that can be used to provide additional information about the semantics of the various elements to assistive technologies like screen readers
	- [ ] Make a better back-end database model design based on many to may relationships
	- [ ] More robust url regex handlers to handle various types of user inputs and requests while maintaining logical consistency
	- [ ] Ability to capture metrics and track usage patterns 
	- [ ] User authentication and autherization to allow CRUD functionailty
	- [ ] Ability to create new user from the home page
	- [ ] More API (JSON) endpoints which filters results according to specific requests and provide CRUD functionality with APIs
	
2. Followed Test Driven Development (TDD) while building the views. However, need to perform more robust and automated testing to ensure proper functionality (Performed manual testing for the features provided in the application and ensured it works properly)

3. SVG's used taken from codepen.io and svgbackgrounds.com

4. Tried utilizing Wikipedia API, but the results were inconsistant and hence utilized Google Books API - (Some functions in the js files may be named wiki, but later switched to Google Books API - so have to change and rename functions appropriately)

5. Tried image resizing with Grunt and some Grunt packages like 'Image Resize'; however the image resizing was not accurate and inconsistant. Hence, did not utilize them.
