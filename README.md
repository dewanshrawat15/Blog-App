# Blog-App
Blog-App is a blogging app. The whole project runs on Django.
- A user can be created by the superuser. Then only can he take edit, delete or add Blog Posts.
- There is a superuser account. Only the superuser can grant or revoke other admin rights.
- Posts can be added from the Django Admin page or a plus sign appears when the admin is logged in.

# Requirement
Any system with python 3 (preferably 3.6) and terminal.

# Usage
- Navigate to the cloned repository.
- Install Django
- Run python manage.py runserver

# Run as docker
- Build project as a docker image by running ```docker build -t blog-app .```
- Run the image as a container and binding it to a port ```docker run --publish 8000:8000 blog-app```
- Run the image as a container and binding it to a port ```docker run -d --publish 8000:8000 blog-app``` to run in detached mode

# Known Issue
None as of now. Feel free to open an issue if any!

# Wanna Contribute ?
Yeah, sure, why not. Just be sure to connect with me at [dewanshrawat.tech](https://dewanshrawat.tech)

# License
> The MIT License
