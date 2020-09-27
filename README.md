# Employee-management

## Using Django REST framework

### This is a simple  Django application for demo to generate a Serialized response from ManyTOMany Relational Database system
* Here I use 2 tables name User and ActivityPeriods.
* User, is for storing Employee details and ActivityPeriods, is for store the start_time and end_time
* Here we have to use manytomany relation for link the employee and his active time log.
* For demonstration purpose i build a custom management command for populate the DB with some sample dummy data by a single command ```python manage.py populate_db```

* Using Django REST framework it is able to genarate a nested JSON structure of all employees details including activity time log.


# Steps

* Create a project folder and create a virtual environment with in your project folder.
* On your terminal within the project folder  type```pip install requirements.txt```  will install all packages which will be needed for this environment.
* clone or download the repository to your project folder. 
* open your terminal at the location where manage.py file is located and type ``` python manage.py migrate``` for migrate database intially
* ```python manage.py createsuperuser``` for create a superuser for as admin.It will ask you to type a username , email,password for your admin panel
* ```python manage.py makemigrations``` and ```python manage.py migrate``` these two commands should use always whenever you make a change in database configuration.
* Run our custom management command ```python manage.py populate_db``` for fill the DB with required format.
* After this much configurations we can run our server by type ```python manage.py``` runserver in our command prompt.It will run the server on port number 8000 by default.
  type the address which the server running and you will get the main page of a django inbuilt REST framework page.
* To add or delete or edit our database further we can go to '/admin' url.Django has very good inbuilt admin panel for this.
* in '/admin' url it will show a login form for enter the admin panel. Type the username and password that you provided when superuser was created.
* You can see new two database entities User ans ActivityPeriods.First add Activity periods start_time and end_time pairs.Then come to User database and add user 
details and you can see a dropdown for activity periods avaliable.Select any number or activity periods and save. We can select multiple activity period objects because its 
manytomany relation.

* After add ActivityPeriods and User with corresponding activity periods go back to out main url('/') and click 'user' link for see nested json object corresponding to 
User and its activity periods
* 'activity period' url at main page will show you the total activity periods in json format.

## For see demo please go to my django application deployment link https://myemployapp.herokuapp.com 
