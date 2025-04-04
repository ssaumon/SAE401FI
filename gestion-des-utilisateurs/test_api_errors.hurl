# Test 1: Register a new user with missing fields
POST http://localhost:5000/register
Content-Type: application/json

{
  "last_name": "Doe",
  "first_name": "John",
  "email": "john.doe@example.com"
}
# Missing "password" and "birth_date" fields
HTTP/1.1 400

# Test 2: Login with incorrect credentials
POST http://localhost:5000/login
Content-Type: application/json

{
  "email": "john.doe@example.com",
  "password": "wrongpassword"
}

HTTP/1.1 401

# Test 3: Get user info with invalid email format
GET http://localhost:5000/user/invalid-email

HTTP/1.1 409

# Test 4: Modify user information with invalid data
PUT http://localhost:5000/modify
Content-Type: application/json

{
  "last_name": "Doe",
  "first_name": "John",
  "email": "invalid-email",
  "password": "newpassword",
  "birth_date": "invalid-date"
}

HTTP/1.1 405

# Test 5: Delete a user with invalid email format
DELETE http://localhost:5000/delete-user/invalid-email

HTTP/1.1 400

# Test 6: Add permissions with missing fields
POST http://localhost:5000/add-permissions
Content-Type: application/json

{
  "project_id": "1",
  "email": "john.doe@example.com"
}
  # Missing "write", "read", and "admin" fields

HTTP/1.1 400

# Test 7: Modify permissions with invalid data
PUT http://localhost:5000/modify-permissions
Content-Type: application/json

{
  "project_id": "1",
  "email": "invalid-email",
  "write": true,
  "read": true,
  "admin": false
}

HTTP/1.1 404

# Test 8: Delete permissions with missing parameters
DELETE http://localhost:5000/delete-permissions

HTTP/1.1 400

# Test 9: Retrieve permissions by project with invalid project ID
GET http://localhost:5000/permissions-by-project/invalid-project-id

HTTP/1.1 409

# Test 10: Retrieve permissions by email with invalid email format
GET http://localhost:5000/permissions-by-email/invalid-email

HTTP/1.1 409
