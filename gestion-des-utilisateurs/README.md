# User Management - REST API

This application is a REST API developed with Flask to manage users and their permissions on different projects.

## Description

The application allows you to:

- Manage users (creation, modification, deletion, login)
- Manage user permissions on different projects
- Store data in JSON files
- Log certain actions

## Servers

- **Main Server**: [http://api.rt.lan/](http://api.rt.lan/)
- **Docker Server**: [http://user:5000](http://user:5000)

## Project Structure

```text
code/
├── app.py           # Main Flask application
├── fonction.py      # Utility functions
└── reset_app.py     # Data reset script
```

## Prerequisites

- Python 3.x
- Flask
- Docker and Docker Compose
- Dependencies listed in `requirements.txt`

## Installation

### Using Docker (Recommended)

1. Clone the repository
2. Build and start the containers:

```bash
docker-compose up --build
```

### Manual Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The application uses three data files:

- `user.json`: User storage
- `permission.json`: Permission storage
- `logs.txt`: Action logs

## Features

### User Management

#### User Registration

- **Endpoint**: `POST /register`
- **Description**: Register a new user
- **Request**:

```json
{
  "last_name": "Doe",
  "first_name": "John",
  "email": "john.doe@example.com",
  "password": "securepassword123",
  "birth_date": "01-01-1990"
}
```

- **Responses**:
  - `200 OK`: User successfully created
  - `400 Bad Request`: Missing field
  - `409 Conflict`: User with this email already exists
  - `415 Unsupported Media Type`: Invalid content type, JSON expected

#### User Login

- **Endpoint**: `POST /login`
- **Description**: Authenticate a user
- **Request**:

```json
{
  "email": "john.doe@example.com",
  "password": "securepassword123"
}
```

- **Responses**:
  - `200 OK`: Login successful
  - `400 Bad Request`: Missing field
  - `401 Unauthorized`: Incorrect password
  - `404 Not Found`: User not found
  - `415 Unsupported Media Type`: Invalid content type, JSON expected

#### Get User Information

- **Endpoint**: `GET /user/{email}`
- **Description**: Get user information
- **Parameters**:
  - `email` (path): User's email address
- **Responses**:
  - `200 OK`: User found
  - `409 Conflict`: User not found

#### Modify User

- **Endpoint**: `PUT /modify`
- **Description**: Update user information
- **Request**:

```json
{
  "last_name": "Doe",
  "first_name": "John",
  "email": "john.doe@example.com",
  "password": "securepassword123",
  "birth_date": "01-01-1990"
}
```

- **Responses**:
  - `200 OK`: User information updated
  - `400 Bad Request`: Invalid request
  - `409 Conflict`: User does not exist

#### Delete User

- **Endpoint**: `DELETE /delete-user/{email}`
- **Description**: Delete a user
- **Parameters**:
  - `email` (path): Email of user to delete
- **Responses**:
  - `200 OK`: User successfully deleted
  - `400 Bad Request`: Invalid request

### Permission Management

#### Add User Permissions

- **Endpoint**: `POST /add-permissions`
- **Description**: Add permissions for a user
- **Request**:

```json
{
  "project_id": "1",
  "email": "john.doe@example.com",
  "write": true,
  "read": true,
  "admin": false
}
```

- **Responses**:
  - `200 OK`: Permissions successfully added
  - `400 Bad Request`: Invalid request
  - `404 Not Found`: User not found
  - `409 Conflict`: Permissions already exist

#### Modify User Permissions

- **Endpoint**: `PUT /modify-permissions`
- **Description**: Update user permissions
- **Request**:

```json
{
  "project_id": "1",
  "email": "john.doe@example.com",
  "write": true,
  "read": true,
  "admin": false
}
```

- **Responses**:
  - `200 OK`: Permissions successfully updated
  - `400 Bad Request`: Invalid request
  - `404 Not Found`: Permissions not found

#### Delete User Permissions

- **Endpoint**: `DELETE /delete-permissions`
- **Description**: Delete user permissions for a project
- **Parameters**:
  - `project_id` (query): Project ID
  - `email` (query): User's email address
- **Responses**:
  - `200 OK`: Permissions successfully deleted
  - `400 Bad Request`: Invalid request
  - `404 Not Found`: User or permissions not found

#### Get Permissions by Project

- **Endpoint**: `GET /permissions-by-project/{project_id}`
- **Description**: Get all permissions for a project
- **Parameters**:
  - `project_id` (path): Project ID
- **Responses**:
  - `200 OK`: Permissions successfully retrieved
  - `400 Bad Request`: Invalid request
  - `409 Conflict`: No permissions found for this project

#### Get Permissions by Email

- **Endpoint**: `GET /permissions-by-email/{email}`
- **Description**: Get all permissions for a user
- **Parameters**:
  - `email` (path): User's email address
- **Responses**:
  - `200 OK`: Permissions successfully retrieved
  - `400 Bad Request`: Invalid request
  - `409 Conflict`: No permissions found for this user

## Code Details

### Utility Functions (`fonction.py`)

#### JSON Operations

- `read_json(filename)`: Reads and validates JSON files
- `write_json(filename, data)`: Writes data to JSON files

#### User Management Functions

- `get_object_by_email(json_data, search_email)`: Finds user by email
- `modify_user_by_email(users, last_name, first_name, email, password, birth_date)`: Updates user data
- `get_user_by_email(users, email)`: Retrieves user data (without password)
- `delete_user_by_email(users, email)`: Removes user from the system

#### Permission Management Functions

- `get_permissions_by_project(json_perm, project_id)`: Gets project permissions
- `get_permissions_by_email(permissions_list, email)`: Gets user permissions
- `get_perm_email_idproject(json_perm, email_id, project_id)`: Finds specific permission

#### Data Purification

- `purify_field(value)`: Cleans and validates input data

### Reset Application (`reset_app.py`)

- Initializes default data in JSON files
- Handles file creation and validation
- Provides default user and permission data

## Usage

### Using Docker

```bash
docker-compose up --build
```

### Manual Start

```bash
python code/app.py
```

The API will be available at `http://localhost:5000`

## Security Considerations

- Passwords are stored in plain text (needs improvement)
- No JWT token system (needs implementation)
- Basic input validation (needs enhancement)
- No rate limiting implemented
- No HTTPS by default

## Possible Improvements

1. Implement password hashing
2. Add JWT authentication system
3. Enhance data validation
4. Add unit tests
5. Implement a database instead of JSON files
6. Add Swagger/OpenAPI documentation
7. Implement a more robust logging system
8. Add rate limiting
9. Enable HTTPS by default
10. Add input sanitization
11. Implement session management
12. Add API versioning

## What can I do better

1. Better test on the API
2. Standardize function outputs, always return `[]` for empty results
3. Improve code organization and readability
