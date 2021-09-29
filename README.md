DjaNext

integrate Django and Nextjs to run on one port
This is a great SaaS MVP maker

Inpired by this video
https://www.youtube.com/watch?v=LJjlEPKxDyw
and his repo: https://github.com/AbukoS/DjangoNextJs_integrate/tree/main/public
I give him all the credits

-

- start by installing nextjs into your desired directory: npx create-next-app
- then cd into new installed directory and run: "npm run dev"
- then create and activate a virtual enviroment
- install django in the virtual enviroment
- then install "django-admin startproject mysite . " <-- (the dot at the end is veryimportant)
- now build your nextjs and django api as usual

# ##### After completing the nextjs/djang project and you are ready to launch the site, do the following

# 1. npm run build

# 2. npx next export -o output

# Make sure you delete the old static folder in your route directory before you continue

# 3. mv output static

# 4. python djanext.py -d static

# 5. python manage.py runserver
