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
1. `__init__.py`
2. settings.py (where you store project settings)
3. url.py (Python script that will store all the URL patterns for your project. Basically the different pages of your web application)
4. wsgi.py (This is a python script that acts as the web server gateway interface. It will later on help us deploy our web app to production)

In the top level directory you will see
1. `manage.py`: This is a python script. It will be associated with many commands as we build our web app.

Let's user `manage.py` now:
```
python manage.py runserver
```


1. User requests URL
2. urls.py
3. views.py
4. models.py
5. Database
6. models.py
7. views.py
8. Templates (HTML, CSS, Javascript)
9. Sends back to User

Django Project: is a collection of applications and configurations taht when combined together will make up the full web application (your complete website running with Django)

Django Application: Created to perform a particular functionality for your entire web application. For example, you can have a registration app, a polling app, a comments app, etc.

These Django Apps can then be plugged into other Django Projects, so you can reuse them! 

Let's create a simple application with:

```
python manage.py startapp firstapp
```

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

Recommendations from Michael King
1. Single page app
2. 
