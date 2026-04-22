# Philford Attendance API

Philford Institute is an ESL(English as Second Language) based in Ghana.
I am building an API for the school, where anytime student registers to join Philford their registration details are taken for them to be able to enroll.
Anytime **Student** or **Teacher** comes to school they show their card to the system to mark them as present in school today. It has time student or teacher is supposed to come too school if a student comes after the time they are supposed to be in class they are late **ADMINS** get notified and they will face the consequences. Passwords are being using **bcrypt** and saved in DB.
A RESTful Attendance API built with **FASTAPI**, **SQLALCHEMY**, **JWT Authentication**, **File Uploads & Validation**, **Authorization**, **PostgreSQL** 

## Features
- User Registration & Login (JWT Auth)
- Student, Teachers(CRUD)
- Attenddance (CRUD & Main Purpose of building)
- Role Based Access Control(RBAC)
- PostgreSQL Integration
- Depedencies Injection to help protect routes
- Error Handling using HTTPException and status codes


## Tech Stack

- **Python3**
- **FASTAPI**
- **SQLALCHEMY**
- **PostgreSQL**
- **Passlib bcrypt**
- **Git & GitHub**


## NOTE:
This project is incommplete needs refactor, these are the following left to complete this project;
- **Async** to make the respond to request faster and smartly
- **Email Verification and Validation** to confirm token and see user already has an account
- **background task** to script and send notifications and other features automatically not  manually
- **WebSocket** for real time notifcation to users
- **Dashboard** using SQL to make ADMIN's dashboard and other analytics


## Project Stucture

C:.
│   config.py
│   database.py
│   enums.py
│   main.py
│   README.md
│
├───ATTENDANCE
│       attedance_routes.py
│       attendance_crud.py
│       attendance_models.py
│       attendance_schemas.py
│       __init__.py
│
├───auth
│       auth_crud.py
│       auth_routes.py
│       auth_schemas.py
│       dependencies.py
│       hashing.py
│       token.py
│       __init__.py
│
├───migrations
│       __init__.py
│
├───STUDENT
│       student_crud.py
│       student_models.py
│       student_routes.py
│       student_schemas.py
│       __init__.py
│
├───TEACHER
│       id_card_uploads.py
│       teachers_crud.py
│       teachers_models.py
│       teachers_routes.py
│       teachers_schemas.py
│       __init__.py
│
├───test
│   │   test_auth.py
│   │   test_user.py
│   │   __init__.py
│   │
│   └───__pycache__
│           test_auth.cpython-313-pytest-8.4.1.pyc
│           test_user.cpython-313-pytest-8.4.1.pyc
│           __init__.cpython-313.pyc
│
├───USER
│       profile_picture.py
│       user_crud.py
│       user_models.py
│       user_routes.py
│       user_schemas.py
│       __init__.py
│
└───__pycache__
        config.cpython-313.pyc
        database.cpython-313.pyc
        main.cpython-313.pyc
        __init__.cpython-313.pyc

## Relationships
- **USER** is relaated to **Teacher**, **Student**, **ADMINS**
- **ATTENDANCE** is related to all the modules.
