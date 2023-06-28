# CookBook - API

## Project Aim
The aim of this project was to build the backend api of my portfolio project 5 - CookBook.
CookBook is a online food blog, where users can read, like and comment on other users recipe blogs as well as create and share their own recipes. They are also able to follow other users and create a shopping list that they can edit to make sure they have exactly what they need to cook the recipes they want.
This was built using Django Rest Framework, Heroku, Cloudinary and ElephantSQL. The cookbook-api has been connected to the front-end of the website (links below).

### Link to deployed Back-End
https://cookbook-project-5.herokuapp.com/

### Link to deployed Front-End
https://cookbook-react-project-5.herokuapp.com/


## Project Goals & Testing
The goals were manually tested when testing the front end, to see if the backend was linked correctly.

| Feature Tested / Project Goals  | Steps taken          | Results |  Link to URL |
|------------------------------|-----------------------------|----------|------------------|
| Create **Posts App** with CRUD functionality. | As a logged in user in the front-end I created a post, edited a post and deleted a post.| ✓ - New post created were added to the back-end posts. Edited posts changed the information in the back-end and deleted posts where deleted in the back-end. | [Link to Posts](https://cookbook-project-5.herokuapp.com/posts) |
|Create **Likes App** that allows users to like and unlike other users posts if they are logged in.| As a logged in user in the front-end I would like and unlike posts. | ✓  - liking a post would add it to back-end likes, and unliking it would delete it from the likes page.| [Link to likes](https://cookbook-project-5.herokuapp.com/likes) |
|Create **Comments App** with CRUD functionality. | As a logged in user in the front-end I would create, edit and delete comments.| ✓ - In the back-end created comments appeared in the comments page, edited comments changes were logged in the back-end and deleted comments were deleted from the back-end comments page. | [Link to comment](https://cookbook-project-5.herokuapp.com/comments) 
|Create **Profiles App** which allows me to create and edit my profile. | As a logged in user in the front end I would sign up for a new account and edit details about my account. | ✓ - Creating a new account added it to the profiles page in the back-end. Editing username or profile bio details about my account were logged in the back-end.| [Link to Profiles](https://cookbook-project-5.herokuapp.com/profiles) |
| Create **Followers App** that allows users to follow/ unfollow other users. | As a logged in user I would try to follow users, and unfollow previously followed users. | ✓ - this would change the "followers_count" and "following_count" in the profiles page accordingly.| [Link to Followers](https://cookbook-project-5.herokuapp.com/followers) |
| Create a **Shopping List App** with CRUD functionality. | As a logged in user I attempted to add, edit and delete items on my shopping list. | ✓ - worked in the front end, and when logged in as admin in the backend, this could also be seen on the shoppinglist page. |
| Manually test each app for functionality of **cookbook_api** | As a user, use all of the apps for their intended purposes. | ✓ - site works as expected, all URL paths worked without error. | [Link to api](https://cookbook-project-5.herokuapp.com/) |


## Features
CookBook api consists of 6 apps.
### Posts
- Users are able to create, read, edit and delete posts if they are logged on.

![api home](https://github.com/dhrutibhudia97/cookbook-api/assets/107180641/757f9d6f-a861-4e0b-ae73-27d1e0fbd42b)


### Profiles
- Users are able to sign up or sign in, and then edit their own profiles by changing their username, password, bio and picture. 
- They are also able to view the most popular profiles.

![api profiles](https://github.com/dhrutibhudia97/cookbook-api/assets/107180641/1a9db861-5e82-483e-91b5-90e10b178aa6)


### Likes
- Users are able to like and unlike other users posts, if they are logged in.

![api likes](https://github.com/dhrutibhudia97/cookbook-api/assets/107180641/bc6ce780-29ab-4db1-878c-4961187e1ab6)


### Comments
- Users are able to create, read, edit and delete comments they make either on their own posts or other users posts, if they are logged in.

![api comments](https://github.com/dhrutibhudia97/cookbook-api/assets/107180641/2283ebf8-729d-4c56-81ec-25efbd660669)

### Followers
- Users are able to follow and unfollow other users if they are logged in.

![api followers](https://github.com/dhrutibhudia97/cookbook-api/assets/107180641/5976f4d3-2efe-49d1-8a6d-6362656b8da4)


### Shopping List
- Users are able to create, read, edit and delete items they can put onto their own shopping lists, if they are logged in.

![shoppinglist backend](https://github.com/dhrutibhudia97/cookbook-api/assets/107180641/f7d95696-109d-407c-a054-f61ad091c034)


## Validators 
- https://pep8ci.herokuapp.com/# was used to validate all python code files (admin.py, apps.py, models.py, serializer.py, tests.py, urls.py and views.py) in cookbook_api, comments, likes, posts, profiles, followers and shoppinglist.
- A few exceptions not passing were a few lines in settings.py (line 121, 170, 173, 176 and 179).
- Screenshots for all files in python validator are found in the files in the main branch "Cookbook-api". Links to these pdfs are below (also found in main branch):

  - https://github.com/dhrutibhudia97/cookbook-api/blob/main/api-python-validator-cookbook.api.pdf
  - https://github.com/dhrutibhudia97/cookbook-api/blob/main/api-python-validator-posts.pdf
  - https://github.com/dhrutibhudia97/cookbook-api/blob/main/api-python-validator-profiles.pdf
  - https://github.com/dhrutibhudia97/cookbook-api/blob/main/api-python-validator-likes.pdf
  - https://github.com/dhrutibhudia97/cookbook-api/blob/main/api-python-validator-comments.pdf
  - https://github.com/dhrutibhudia97/cookbook-api/blob/main/api-python-validator-followers.pdf
  - https://github.com/dhrutibhudia97/cookbook-api/blob/main/api-python-validator-shoppinglist.pdf


## Deployment Steps (GitHub, Gitpod, Heroku, ElephantSQL and Cloudinary)
1. I created a repository in Github using the https://github.com/Code-Institute-Org/react-ci-template/ template and named it "cookbook-api".

2. On https://heroku.com/ I created a new app called "cookbook-project-5".

3. On https://www.elephantsql.com/ I logged in with my Github account and created a new instance "Cookbook".

4. I added the PostgreSQL to the Config Vars of heroku app under DATABASE_URL.

5. In Gitpod, in the terminal install the following:
  - $ django-admin startproject cookbook-api
  - $ pip install 'django<4'
  - $ pip install django-cloudinary-storage
  - $ pip install Pillow
  - $ pip install djangorestframework
  - $ pip install django-filter
  - $ pip install dj-rest-auth==2.1.9
  - $ pip install 'dj-rest-auth[with_social]'
  - $ pip install djangorestframework-simplejwt
  - $ pip install dj_database_url=0.5.0 psycopg2
  - $ pip install gunicorn django-cors-headers

6. In heroku/settings, add to Config Vars: ( Keys: Value)
  - ALLOWED_HOST : "link to deployed api app"
  - CLIENT_ORIGIN : "link to deployed react app"
  - CLIENT_ORIGIN_DEV : "link to working link when you run "$npm start" in the terminal of the front-end app on gitpod"
  - CLOUDINARY_URL : found in your own cloudinary account under API Environment Variable.
  - DATABASE_URL : found in your ElephantSQL account.
  - DISABLE_COLLECTSTATIC : 1
  - HEROKU_POSTGRESQL_TEAL_URL : found in your ElephantSQL account.
  - SECRET_KEY : Make this up and don't share it.

7. In Gitpod create an env.py file in the same level as the cookbook_api, then add links for these found above in step 6. :
    import os
    os.environ['CLOUDINARY_URL'] = "______"
    os.environ['SECRET_KEY'] = "______"
    os.environ['DEV'] = 1
    os.environ['DATABASE_URL'] = "______"

8. In Gitpod in settings.py make sure your "INSTALLED_APPS" include:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',
    'profiles',
    'posts',
    'comments',
    'likes',
    'followers',
    'shoppinglist',

9. Add a Procfile to your Gitpod, same level as cookbook_api, add:
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn cookbook_api.wsgi

10. Create a requirements.txt file on the same level as cookbook_api by typing in the terminal:
  - $ pip freeze > requirements.txt 

11. Migrate your changes in the terminal:
  - $ python manage.py makemigrations
  - $ python manage.py migrate

12. Commit the changes to GitHub.

13. In Heroku deploy the app.


## Unfixed Bugs
- No unfixed bugs I am aware of in the CookBook-API.


## Technologies used
- GitHub
- Gitpod
- Heroku
- ElephantSQL
- Cloudinary

### Languages
- Python
- Dockerfile
- Shell
- Procfile

### Framework
- Django Rest Framework

### Software Installed
- Cloudinary
- Pillow
- Psycopg2
- Django Rest Framework Authentication
- Gunicorn
- Django Cross-Origin Resource Sharing (CORS)


## Credits and Acknowledgements
- This CookBook api was based on the **Code Institutes Django Rest Framework module**, especially on the: Post, Likes, Comments and Followers apps. I then customised the post model and added the shoppinglist model to help achieve my project goal.
- Tutor Assistance for helping solve bugs and error codes.
- My mentor Adegbenga Adeye for helping with ideas to add to this app.

