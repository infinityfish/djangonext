# ##### Welcome to DjangoNext

Integrate Django and Nextjs to run on one port
This is a great SaaS MVP starter
Host your project with any hosting service that can handle python and postgres or your DB of choice

# ##### Intsallation: You can just clone this repo and start from there, or you can follow the instructions below. make sure that you install everything in DjangoNext's requirements.txt

- start by installing nextjs into your desired directory: npx create-next-app
- then cd into new installed directory and run: "npm run dev" to test your frontend
- then create and activate a virtual enviroment
- install the requirements.txt file
- then install "django-admin startproject mysite . " <-- (the dot at the end is very important: both nextjs's package.json and django's manage.py will be in the same folder)
- now build out your nextjs and django api as usual

# ##### After completing the nextjs/django project and you are ready to launch the site, do the following

# 1. npm run build

# 2. npx next export -o output

# Make sure you delete the old static folder in your route directory before you continue. We are going to create a new one below with the uptodate frontend.

# 3. mv output static

# 4. python djangonext.py -d static

# 5. python manage.py runserver

Inpired by this video
https://www.youtube.com/watch?v=LJjlEPKxDyw
and his repo: https://github.com/AbukoS/DjangoNextJs_integrate/tree/main/public
I give him all the credits

-
