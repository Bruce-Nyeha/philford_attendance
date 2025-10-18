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

- **Python(Core Language)**
- **FASTAPI**
- **SQLALCHEMY**
- **PostgreSQL**
- **Pass bcrypt**
- **Git & GitHub**


## NOTE:
This project is incommplete needs refactor, these are the following left to complete this project;
- **Async** to make the respond to request faster and smartly
- **Email Verification and Validation** to confirm token and see user already has an account
- **background task** to script and send notifications and other features automatically not  manually
- **WebSocket** for real time notifcation to users
- **Dashboard** using SQL to make ADMIN's dashboard and other analytics


## Project Stucture

philford_attendance_api
        ⬇
       app ➡️ config ➡️ database ➡️ enums ➡️ main ➡️ README
        ⬇
ATTENDANCE | auth       | migrations  | STUDENT | TEACHER | USER 
    ⬇          ⬇             ⬇           ⬇          ⬇       ⬇
models     |            |             |models   |models   |models
schemas    |schemas     |             |scehmas  |schemas  |schemas
crud       |crud        |             |crud     |crud     |crud
routes     |routes      |             |routes   |routes   |routes
           |dependencies|
           |hashing
           |token


## Relationships
- **USER** is relaated to **Teacher**, **Student**, **ADMINS**
- **ATTENDANCE** is related to all the modules.