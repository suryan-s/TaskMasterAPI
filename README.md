# TaskMasterAPI 🚀

TaskMasterAPI is an API-based solution built using Django Rest Framework with JWT authentication. It provides a comprehensive set of endpoints to manage tasks and user accounts programmatically.

## Features ✨

* User Registration: ✅ Users can create an account by sending a POST request to `/api/account/register/` with the required details (name, email, and password). Upon successful registration, users can proceed to login.
* Login: 🔐 Registered users can authenticate themselves by sending a POST request to `/api/account/login/` with their email and password. If the login request is successful, an access token and refresh token will be provided in the response.
* Logout: 🚪 Users can log out by sending a POST request to `/api/account/logout/` with their refresh token. Upon successful logout, a "Logout successful" message will be returned.
* Access Token Refresh: ♻️ Users can obtain a new access token by sending a POST request to `/api/account/token/refresh/` with their refresh token. This allows users to extend their session without having to reauthenticate.
* Task Management: 📝 The API provides endpoints for managing tasks. Users can retrieve their ongoing, completed, and expired tasks by sending a GET request to `/api/home/`. To add a new task, users can send a POST request to `/api/home/add/` with the required task details (title, description, and deadline_at). Users can mark a task as completed by sending a POST request to `/api/home/complete/` with the task ID.

## API Endpoints 🛠️

1. **Register**: `POST /api/account/register/`

Request Body:

```
{
    "name": "sample_name",
    "email": "sample_mail@gmail.com",
    "password": "sample_password"
}
```

2. **Login**: `POST /api/account/login/`

Request Body:

```
{
    "email": "sample_mail@gmail.com",
    "password": "sample_password"
}
```

3. **Logout**: `POST /api/account/logout/`

Request Body:
```
{
    "refresh_token": "your_token"
}
```

4. **Access Token Refresh***: `POST /api/account/token/refresh/`

Request Body:
```
{
    "refresh": "your_token"
}
```

5. **Get Tasks**: `GET /api/home/`
Would return 3 lists : ongoing, completed and expired.

6. **Add Task**: `POST /api/home/add/`

Request Body:

```
{
    "title": "Sample Task",
    "description": "This is a sample task.",
    "deadline_at": "2023-06-10T12:00:00"
}
```

7. **Mark Task as Completed**: `POST /api/home/complete/`

Request Body:

```
{
    "id": 1
}
```

***Note: All requests except login and register must include the access token as the bearer authentication header.***

## Deployment 🌐

TaskMasterAPI is hosted on Render.com and can be accessed using the following link: https://taskmasterapi.onrender.com/

## Technologies Used 💻

- Django Rest Framework: A powerful framework for building APIs with Django.
- JWT Authentication: Token-based authentication using JSON Web Tokens.
- Render.com: A cloud platform for deploying and managing web applications.

## Usage 🚀

To utilize the TaskMasterAPI, follow the endpoint descriptions provided above and make requests to the respective URLs using a tool like cURL or postman.
