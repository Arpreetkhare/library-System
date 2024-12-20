# Library Management System

A Flask-based Library Management System that supports CRUD operations for managing books and members. This project is built with Flask, SQLAlchemy, and MySQL.

---

## Features
- **Manage Books**: Add, update, delete, and view books.
- **Manage Members**: Add, update, delete, and view members.
- **Pagination**: View members and books in a paginated format.
- **Database**: MySQL database integration using SQLAlchemy ORM.

---

## API Endpoints

### Member Management

| HTTP Method | Endpoint               | Description                         |
|-------------|------------------------|-------------------------------------|
| GET         | `/members/<id>`         | Get details of a specific member    |
| POST        | `/members`              | Add a new member                    |
| PUT         | `/members/<id>`         | Update an existing member           |
| DELETE      | `/members/<id>`         | Delete a specific member            |

---

### Book Management

| HTTP Method | Endpoint               | Description                         |
|-------------|------------------------|-------------------------------------|
| GET         | `/books/<id>`           | Get details of a specific book      |
| POST        | `/books`                | Add a new book                      |
| PUT         | `/books/<id>`           | Update an existing book             |
| DELETE      | `/books/<id>`           | Delete a specific book              |


## Installation Guide

### Step 1: Clone the Repository
To begin, clone the repository to your local system:
  ```bash
  git clone https://github.com/username/library-system.git
  cd library-system
```

### step 2: Set Up a Virtual Environment
  ```bash
  python3 -m venv venv
  source venv/bin/activate
```
### Step 3: Install Dependencies
  ```bash
  pip install -r requirements.txt
```

