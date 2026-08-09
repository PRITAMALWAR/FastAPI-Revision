

📁 FastAPI is a modern, high-performance web framework used for building RESTful APIs with Python.


📁 All Lesson 
 
- Lesson 1 Hello FastAPI
- Lesson 2 Path & Query Parameters
- Lesson 3 POST Requests
- Lesson 4 Pydantic Models
- Lesson 5 CRUD API
- Lesson 6 SQLite Database
- Lesson 7 SQLAlchemy
- Lesson 8 JWT Authentication
- Lesson 9 File Upload
- Lesson 10 Deployment
- Final Project (any Project With User Authentication API)


Most -

- python3 -m venv .venv
- sudo apt update
- sudo apt install python3-venv
- source .venv/bin/activate
- python -m pip install fastapi uvicorn
- python -m uvicorn --version
- python -m uvicorn main:app --reload --port 8001



📁 HTTP status


- 200	Success
- 201	Created
- 400	Bad Request
- 401	Unauthorized
- 403	Forbidden
- 404	Not Found
- 500	Server Error



SQLite Process

- Activate your .venv = Activate your .venv
- python --version

- Check FastAPI and Uvicorn 
- python -m pip show fastapi

- Check SQLite
- python -c "import sqlite3; print(sqlite3.sqlite_version)"

- python -m uvicorn main:app --reload





- JWT 

- python -m pip install fastapi uvicorn sqlalchemy PyJWT "pwdlib[argon2]" python-multipart

- python -c "import fastapi, uvicorn, sqlalchemy, jwt, pwdlib, multipart; print('All Lesson 8 packages OK')"

- python -m uvicorn main:app --reload


