# Login Form Mechanism By Using Django Framework
---
This project contains the logic of Registration and Login pages. It contains 3 Pages. **1.Home Page**  **2.Login Page**  **3.Registration Page**.
Submit the data into the Registration page. And Login  to the page by corresponding **username** and **password** then it will show the message "**Login Success**" and if the user doesn't exist it will show the message "**Login Failed**".

It contains 3 Folders
---

1. Project Folder **login** 
2. App Folder **regandloginapp**
3. Template Folder **template**

## Requirements and Installation
---

1. [Python setup guide](https://www.howtogeek.com/197947/how-to-install-python-on-windows/)<br>
2. [django installation guide](https://docs.djangoproject.com/en/2.0/howto/windows/)<br>
3. [Mysql installation guide](https://dev.mysql.com/downloads/installer/)<br>

### settings.py
---
**Database Part**

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbadmin',
        'USER': 'USERNAME',       #set your database USERNAME
        'PASSWORD': 'PASSWORD',   #set your database PASSWORD

    }
}
```
* Create the database to the corresponding database name mentioned above the Database code.
>create database dbadmin;

Do **migrate** and **makemigrations**


* Run the Server
> python manage.py runserver


* Copy the IPaddress
>Starting development server at http://127.0.0.1:8000/


* add "regandloginapp" after **/** in the url of a Browser.
>"http://127.0.0.1:8000/regandloginapp/"

 After that Home Page will come.
 Do registration and login operation.<br>
 
 Ok **Happy Coding**..  :thumbsup:  :smile: !!
 
