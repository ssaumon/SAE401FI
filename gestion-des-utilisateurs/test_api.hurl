# reset 
GET http://localhost:5000/reset_json
HTTP/1.1 200

# Test 1: Register a new user
POST http://localhost:5000/register
Content-Type: application/json
{
  "last_name": "Doe",
  "first_name": "John",
  "email": "john.doe3@example.com",
  "password": "securepassword123",
  "birth_date": "1990-01-01"
}

HTTP/1.1 200

# Test 2: User login
POST http://localhost:5000/login
Content-Type: application/json
{
  "email": "john.doe3@example.com",
  "password": "securepassword123"
}

HTTP/1.1 200

# Test 3: Get user info
GET http://localhost:5000/user/john.doe@example.com

HTTP/1.1 200

# Test 4: Modify user information
POST http://localhost:5000/modify
Content-Type: application/json

{
  "last_name": "Doe",
  "first_name": "John",
  "email": "john.doe@example.com",
  "password": "newsecurepassword123",
  "birth_date": "1990-01-01"
}

HTTP/1.1 200

# Test 5: Delete a user
DELETE http://localhost:5000/delete-user/john.doe3@example.com

HTTP/1.1 200

# Test 6: Add user permissions
POST http://localhost:5000/add-permissions
Content-Type: application/json

{
  "project_id": "3",
  "email": "john.doe@example.com",
  "write": true,
  "read": true,
  "admin": false
}

HTTP/1.1 200

# Test 7: Modify user permissions
PUT http://localhost:5000/modify-permissions
Content-Type: application/json

{
  "project_id": "1",
  "email": "john.doe2@example.com",
  "write": false,
  "read": true,
  "admin": true
}

HTTP/1.1 200

# Test 8: Delete user permissions
DELETE http://localhost:5000/delete-permissions?project_id=1&email=john.doe@example.com

HTTP/1.1 200

# Test 9: Get permissions by project
GET http://localhost:5000/permissions-by-project/2

HTTP/1.1 200

# Test 10: Get permissions by email
GET http://localhost:5000/permissions-by-email/john.doe2@example.com

HTTP/1.1 200
