# Github_user_API

A simple Django framework based project to -

* Search Github Users using username and retrieve the user's data
* Monitor this app using Django admin panel
* User_info model includes organised table with a search bar where you can search on basis of name of the user and date when the user was searched
* Models added for API requests per day/month/year.

## Prerequisites

You will need Django framework to run this project smoothly. Go to your terminal and execute the following command or visit [Django](https://www.djangoproject.com/) website.

```
pip install django
```
or

```
pip3 install django
```
### How to run the project

Step by step explanation of the project -

* Enter the project directory.
* Make migrations for the project -

```
python manage.py makemigrations
```

* Migrate the changes -

```
python manage.py migrate
```

* Create SuperUser-

```
python manage.py createsuperuser

Provide username, email and password to login!
Default added = username - admin | password - Abcd@1234
```

* Run the server -

```
python manage.py runserver
```

* Access http://127.0.0.1:8000/app on your browser to use the application.

### Usage

* Add username in search bar and hit 'Make Request' to retrieve user data.<br />

![Screenshot](/Pictures/api_page.png)

<br /><br />
* Access http://127.0.0.1:8000/admin on your browser for Admin panel and authenticate <br />
![Screenshot](/Pictures/admin_home.png)

<br />
* Choose 'User_info' to access user data table to see all API calls.<br />
![Screenshot](/Pictures/user_table.png)

<br />
* Use Search bar to filter data according to fields given in table.<br />
![Screenshot](/Pictures/search_bar.png)



## Authors

* **Abhishek Singh** - Love python and everything related to it (Email - absinghemail@gmail.com)


## Acknowledgments

* StackOverFlow xD
* Django Documentation FTW

