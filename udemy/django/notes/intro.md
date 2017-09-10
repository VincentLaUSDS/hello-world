# What is the web?

What happens when you're at home and you open up a website.
You start off by typing the URL into your browser

Your computer then sends this request as a packet, which includes the IP Address of the website you want.

It sends this request through wires, or a satellite which eventually links to wires using your ISP

Your ISP will then re-route the request to the appropriate server location, using the IP address as the guide

Once your request reaches the server, it can send back the website you were asking for. However, a full website with content is too big to send back in single packet of data

server sends back website with many packets

The packets come back with instructions how to reassemble themselves.

# What does full stack mean?
There are two main components of a website

## Front End
This is what you see as a user

1. HTML: HyperText Markup Language
2. CSS: Cascading Style Sheets. Colors, fonts, borders, etc. are all described by CSS
3. Javascript: Allowed you to add interactivity to the website, including programming logic.

## Back end
The technology used to actually decide what yo show you on the front end

The backend has three components 
1. The Language (e.g. Python)
2. The Framework (e.g. Django)
3. The Database (e.g. Postgres)

Technologies such as PhP, Node.js, Ruby/Rails, are all viable

# How does Django Work?
Django is a free and open source framework. It allows us to do two things:
1. Map a requested URL from a user to the code meant to handle it
2. Recreate the request URL dynamically.

We can inject values from say, a database, to HTML to show to the user. The framework allows us to connect all the front end stuff with the backend stuff.

To create a virtual environment with conda

```
conda create --name myEnv django
activate myEnv
```

When you install Django, it actually also installed a command line tool called: `django-admin`

Let's create our first project. Type:
```
django-admin startproject first_project
```

When you do that you will see 4 files under `first_project` directory
1. `__init__.py`: Let's Python know this directory can be treated as a package
2. settings.py (where you store project settings)
3. url.py (Python script that will store all the URL patterns for your project. Basically the different pages of your web application)
4. wsgi.py (This is a python script that acts as the web server gateway interface. It will later on help us deploy our web app to production)

In the top level directory you will see
1. `manage.py`: This is a python script. It will be associated with many commands as we build our web app.

Let's use `manage.py` now:
```
python manage.py runserver
```

The first time you run this, you might see something like:
```
You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

A migration allows you to move databases from one design to another, this is also reversible. 

1. User requests URL
2. urls.py
3. views.py
4. models.py
5. Database
6. models.py
7. views.py
8. Templates (HTML, CSS, Javascript)
9. Sends back to User

Difference between Django Project vs. App

Django Project: is a collection of applications and configurations that when combined together will make up the full web application (your complete website running with Django)

Django Application: Created to perform a particular functionality for your entire web application. For example, you can have a registration app, a polling app, a comments app, etc.

These Django Apps can then be plugged into other Django Projects, so you can reuse them! 

Let's create a simple application with:

```
python manage.py startapp firstapp
```

Let's look at the files that were created for us under the `firstapp` directory
1. __init__.py
2. admin.py: Can register your models here which Django will then use them with Django's admin interface
3. apps.py: Here you can place application specific configurations.
4. models.py: Here you store the application's data models.
5. tests.py: Here you can store test functions to test your code.
6. views.py: This is where you have functions that handle requests and return responses.
7. migrations directory: this directory stores database specific information as it relates to models. 

Need to tell django about firstapp's existence.
1. Go back to settings.py and add firstapp
2. Then create a view, map to url to complete the process.

We can then (1) by going to `settings.py` and adding
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstapp',
]
```

## Hello world app
In `views.py` create your first view by doing:
```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World')
```

1. Each view, is going to exist in `views.py` as its own function
2. In this case, we created one view, called `index`. Each view takes in at least one argument. For HttpRequest object, because it lives in Django Http module, by convention, we call it `request`. Note this is just a variable name, you can name it whatever you want.
3. Each view must return an HttpResponse object.
4. Instead of a string, we could pass in HTML object.
5. We now need to map this view to the url in `urls.py`.  

## Django URL Mapping
Previously, we showed a very direct mapping from the views.py to the urls.py 

Now, we want to show the ability of using the `include()` function from `django.conf.urls`

The `include()` function allows us to look for a match with regular expressions and link back to our application's own `urls.py` file.

So for example, we can add the following to our project's `urls.py` file. 

```
from django.conf.urls import include
urlpatterns = [
    url(r'^firstapp/', include('firstapp.urls'))
]
```

This will include all the urls in `/firstapp/urls.py`. 

This will allow us to look for any url that has the pattern www.domainname.com/firstapp/. If we match the pattern, the `include()` function basically tells Django to go look at the `urls.py` file inside of `firstapp` folder

We will see this is useful because we want to keep our project's urls.py clean and modular.

## Django Templates
Templates are a key part to understand how Django really works and interacts with website

Later on we'll learn how to connect templates with models, so we can display data created dynamically taken straight from the database. For now, let's focus on the basics of templates and template tags.

The template will contain the static parts of an html page 

Then there are template tags, which have their own special syntax. This syntax allows you to inject dynamic content that your Django App's views will produce, effecting the final HTML. 

To get started with templates you first need to create a templates directory and then a subdirectory for each specific app's templates. 

This goes inside of your top level directory 
first_project/templates/firstapp

The next step is to let Django know of the templates by editing the DIR key inside the TEMPLATES dictionary in the settings.py file. However, there is an issue we have to deal with before this!

We want our Django project to be easily transferrable from one computer to another, but the DIR key will require a "hard coded" path. How do we resolve this?

```
import os

print(__file__)
print(os.path.dirname(__file__))
```

We will use this os module to feed the path to the DIR key. 

Once we have done that we can create an html file called index.html inside of the templates/firstapp directory. 

Inside this html file, we will insert template tags (a.k.a. Django Template Variable). These template variables will allow us to inject content into the HTML directly from Django. 

This is now starting to reveal the power of using a web framework. Django will be able to inject content into the HTML. This means we will later on use Python code to inject content from a database!

In order to achieve this, we will use the render() function and place it into our original index() function inside of our views.py file. 

## Working with static files
1. We will create a new directory inside of the project called static (just like we did for templates)
2. Then we will add this directory path to the project's settings.py file
3. We will also add a STATIC_URL variable
4. Once we've done that, we need a place to store our static image files.
5. We create a directory inside of static called images
6. Place a .jpg file inside this images directory (or just download one)

To load a static file in html file,

```
{% load staticfiles %}
```

Then, we want to insert the image with an HTML `<img src= >` style tag using:
```
<img src ={%static "images/pic.jpg" %} />
```

