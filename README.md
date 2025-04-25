# TMS-DjangoREST
The Task Management System is a backend API built with Django REST Framework to manage projects, tasks, comments, and user roles in an organization. It supports role-based access control with five user types: Admin, Project Manager, Project Lead (Tech Lead), Developer, and Client. 

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Server](#running-the-server)
- [API Documentation](#api-documentation)
  - [Base URL](#base-url)
  - [Authentication Endpoints](#authentication-endpoints)
  - [User Endpoints](#user-endpoints)
  - [Role Endpoints](#role-endpoints)
  - [Project Endpoints](#project-endpoints)
  - [Task Endpoints](#task-endpoints)
- [Examples](#examples)

---

## Features

- **User & Role Management**: Create and manage users and their roles (admin, project manager, tech lead, developer, client).
- **Project Management**: CRUD operations on projects with owner and members.
- **Task Management**: CRUD operations on tasks with status, priority, assignment, and due date.
- **Comments**: Add comments to projects or tasks.
- **Authentication**: Token-based authentication with login and logout endpoints.


## Prerequisites

- Python 3.10+
- pip (Python package manager)
- virtualenv (recommended)

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate # On Unix/MacOS
venv\Scripts\activate # On Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Create a superuser (Django-admin Login)

```bash
python manage.py createsuperuser
```

### 5. Running the Server

```bash
python manage.py runserver
```

The API will be available at http://localhost:8000/api/.

## API Documentation

### Base URL

```
http://localhost:8000/api/
```

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|-----------------|---------------------------|
| POST | /users/login/ | Obtain authentication token |
| POST | /users/logout/ | Logout current user |

### User Endpoints

| Method | Endpoint | Description |
|--------|----------------|--------------------------|
| GET | /users/ | List users |
| POST | /users/ | Register a new user |
| GET | /users/{id}/ | Retrieve a specific user |
| PUT | /users/{id}/ | Replace a user |
| PATCH | /users/{id}/ | Partial update of a user |

### Role Endpoints

| Method | Endpoint | Description |
|--------|-----------|------------------------------|
| GET | /roles/ | List roles |

### Project Endpoints

| Method | Endpoint | Description |
|--------|-----------------|-----------------------|
| GET | /projects/ | List/search projects |
| POST | /projects/ | Create new project |
| GET | /projects/{id}/ | Retrieve specific project |
| PUT | /projects/{id}/ | Update project |

### Task Endpoints

| Method | Endpoint | Description |
|--------|---------------|----------------------|
| GET | /tasks/ | List/search tasks |
| POST | /tasks/ | Create task |
| GET | /tasks/{id}/ | Retrieve task |
| PUT | /tasks/{id}/ | Update task |
| DELETE | /tasks/{id}/ | Delete task |

