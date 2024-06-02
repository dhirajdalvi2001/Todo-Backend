# Steps to created the backend

1. `py -m venv venv`
2. `django-admin startproject Backend`
3. `python manage.py startapp Todo`
4. `python manage.py migrate`
5. `python manage.py runserver (to run the server)`

# Setup initial django code

1. Add app name ('todo') in the INSTALLED_APPS list in settings.py
2. Create a model in models.py
3. run command `python manage.py makemigrations`
4. run command `python manage.py migrate`
5. Add TodoAdmin class in admin.py file with list_display and a list of fields for the model
6. Add admin.site.register(Todo, TodoAdmin) at the end of the admin.py file

# Create super user

1. `python manage.py createsuperuser`
2. Enter credentials for the superuser
3. `python manage.py runserver`
4. Go to the localhost server
5. Go to /admin and login using the superuser credentials

# Install rest template related packages
  
1. `pipenv install djangorestframework django-cors-headers`
2. Add 'corsheaders' and 'rest_framework' in INSTALLED_APPS list in settings.py
3. Add 'corsheader.middleware.CorsMiddleware' in MIDDLEWARE list in settings.py
4. Create a file serializers.py 
5. Create a class and add meta inside it with model and field defined
6. Create view class
7. Import todo, rest_framework in urls.py 
8. Add router configuration and also add paths in the urlPatterns