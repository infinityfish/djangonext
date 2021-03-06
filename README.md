# ##### Welcome to DjangoNext

Integrate Django and Nextjs to run on one port
This is a great SaaS MVP starter
Host your project with any hosting service that can handle python and postgres or your DB of choice

# ##### Installation:

You can just clone this repo and start from there, or you can follow the instructions below. make sure that you install everything in DjangoNext's requirements.txt

- start by installing nextjs into your desired directory: npx create-next-app
- then cd into new installed directory and run: "npm run dev" to test nextjs
- then create and activate a virtual enviroment :
  $ python -m venv venv
  $ source venv/bin/activate  
  (windows) venv\Scripts\activate
- install the requirements.txt file
- then create django project "django-admin startproject djangonext . " <-- (the dot at the end is veryimportant)
- test your django installation: python manage.py runserver
- configure static, media and template directories in Django as in the exapmple here. Note that both nextjs and django use the "static" folders. So you have to name the static folder for django "staticdjn" to avoid conflicts.

settings.py, they should look like this:

STATICFILES_DIRS = [
os.path.join(BASE_DIR, 'staticdjn')
]

the templates directory should include:
'DIRS': [os.path.join(BASE_DIR, 'staticdjn')],

- configure urls.py file to add media/static
- now build your nextjs and django api as usual

# ##### After completing the nextjs/django project or doing any updates and you are ready to launch the site, do the following

# 1. Make sure you delete the old "staticdjn" folder in your route directory before you continue. We are going to create a new one below with the uptodate frontend.

- And then "npm run deploy"
  this command will build the nextjs app, move the the static files for django to use and start django server.

Inpired by this video
https://www.youtube.com/watch?v=LJjlEPKxDyw
and his repo: https://github.com/AbukoS/DjangoNextJs_integrate/tree/main/public
I give him all the credits
