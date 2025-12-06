🐾 Zoo Management System (Django + MySQL)

A simple web application built with Django 5 that allows users to browse animals, search information, and manage staff accounts.The project includes three user roles: Visitor, Keeper, and Administrator.

This guide explains how to install and run the project on Windows, Linux, or macOS.

✅ Features

User authentication (login/logout)

Role‑based access:

Visitor: read‑only access

Keeper: manage animals and visits

Administrator: manage users (create, edit, delete)

Animal search page

Custom admin dashboard (not Django admin)

MySQL database support

📦 1. Requirements

You need:

Python 3.10+

MySQL Server 8+

pip (Python package manager)

Git (optional)

📁 2. Clone the project

git clone https://github.com/your-username/zoo-project.git
cd zoo-project

📚 3. Install dependencies

The project includes a requirements.txt file.

✅ Windows

py -m pip install -r requirements.txt

✅ Linux / macOS

python3 -m pip install -r requirements.txt

⚠️ Linux users: install MySQL headers first

Ubuntu / Debian:

sudo apt install default-libmysqlclient-dev build-essential

Fedora:

sudo dnf install mysql-devel

🗄️ 4. Configure the database

Create a MySQL database:

CREATE DATABASE zoo_db CHARACTER SET utf8mb4;

Create a MySQL user (optional):

CREATE USER 'zoo_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON zoo_db.* TO 'zoo_user'@'localhost';
FLUSH PRIVILEGES;

⚙️ 5. Configure Django settings

Edit zoo_project/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zoo_db',
        'USER': 'zoo_user',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

🏗️ 6. Apply migrations

python manage.py migrate

👤 7. Create an admin user

python manage.py createsuperuser

This user can log into Django’s built‑in admin panel at:

http://127.0.0.1:8000/admin/

▶️ 8. Run the server

python manage.py runserver

Open your browser:

http://127.0.0.1:8000/

🧪 9. Default pages

URL

Description

/

Home page

/login/

User login

/recherche/

Animal search

/admin/

Custom admin dashboard (role = 2)

/admin/ (Django admin)

Built‑in admin interface

🛠️ 10. Project structure

zoo_project/
│   manage.py
│   requirements.txt
│
├── zoo_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── zoo_app/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── zoo_app/
            ├── base.html
            ├── accueil.html
            ├── recherche.html
            ├── fiche_animal.html
            ├── login.html
            └── admin.html

✅ 11. Troubleshooting

✅ MySQL client installation fails

Install MySQL development headers (Linux):

sudo apt install default-libmysqlclient-dev

✅ TemplateDoesNotExist

Make sure templates are inside:

zoo_app/templates/zoo_app/

✅ Access denied for user

Check your MySQL username/password in settings.py.


- - - - - - - - - - - - - - - - - - - - -

from barbless1/zmanager :

# Zmanager

This is a repository containing the files of the Zmanager project.

## Description

Zmanager is a simple tool using Django, SQL and HTML as a zoo management website. You can add users, administrators, animals and track medical files.
However this tool was made in an educational context and is not intended to be used by any professional, There is an SQL database template provided. 

## How to install Zmanager 

/!\ As this is only an highschool project, it was made in an educational purpose, you should never use Zmanager in a professional context. 
If you are not a Zoo employee here is how to install Zmanager : 

1. Setting up a database
You will need to set up a database which the website will use to fetch it's data.

The Zmanager production server uses MySQL as it's database, however you can use also use PostGreSQL or MariaDB by making the necessary changes in the Django
`settings.py` file. 

2. Installing Django

After setting up your database correctly, follow the Django installation instructions [Django Install ](https://docs.djangoproject.com/en/6.0/intro/install/).
You can then clone this repository in your project folder and get running.

3. Modifying the static pages 

The `static` folder contains all the .html files that you can modify along with Django database fetches to adjust Zmanager to your liking.

## Usage

Visit http://localhost:port to use the website, you can add users via Django, we recommend using PhpMyAdmin to add informations for the zoo. 

## Contributing
Feel free to submit pull requests or open issues.

## (Un)License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

For more informations : 
[unlicense.org](https://unlicense.org).

## Contact

Email : noapluquet@ik.me

![iguana-8539349_1280](https://github.com/user-attachments/assets/751187db-2f21-4624-a0cb-93ac196563a6)

### QnA 

This is a repository containing the files of the Zmanager project.

What is Zmanager ? 
  - Zmanager is an highschool website project which runs thanks to Django and Mysql.

Is it useful ? 
  - Probably not as i will not provide any update after the end of the project date.

Can i use it for my Zoo ? 
  - No, it will lead to big security concerns if you try to use this education oriented project as a real professional tool

Did you use AI to code the project ? 
  - I am quite sceptic about AI, however i think programmation is a great tool which leads to wonderful projects. AI can be used as long as the developper understands fully what he is doing
    personally i used ChatGPT to plan the project infrastructure, but all HTML files were handwritten (on paper literally, yes), the "production" server was deployed with Portainer aswell.

What are the goals of this project ? 
  - This project was made to obtain a good grade in the NSI subject (Computer science in French schools), however judging by the efficiency of our team i don't think we'll get more than 10/20.

What grade did you get for the project and how did the presentation go ? 
  - This will be answered on 12/13/2025 (Remind me later)

Was it difficult to deploy ?
  - Of course, but positivity and motivation helps with the difficulty of starting the project, don't hesitate with name, appearance etc... at first, just make something and later you'll find inspiration

Will you maker other projects ? 
  - Yes when i'll have free time.

Goodbye ? 
  - Goodbye, see you soon
