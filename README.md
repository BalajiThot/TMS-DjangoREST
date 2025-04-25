# TMS-DjangoREST
The Task Management System is a backend API built with Django REST Framework to manage projects, tasks, comments, and user roles in an organization. It supports role-based access control with five user types: Admin, Project Manager, Project Lead (Tech Lead), Developer, and Client. 

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [API Documentation](#api-documentation)
  - [Base URL](#base-url)
  - [Authentication Endpoints](#authentication-endpoints)
  - [User Endpoints](#user-endpoints)
  - [Role Endpoints](#role-endpoints)
  - [Project Endpoints](#project-endpoints)
  - [Task Endpoints](#task-endpoints)
  - [Comment Endpoints](#comment-endpoints)
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

