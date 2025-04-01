# Test 1: Register a new user with missing fields
POST http://localhost:5000/register
Content-Type: application/json

# Missing "password" and "birth_date" fields
HTTP/1.1 400

# Test 2: Login with incorrect credentials
POST http://localhost:5000/login
Content-Type: application/json

HTTP/1.1 400

# Test 3: Get user info with invalid email format
GET http://localhost:5000/user/

HTTP/1.1 404

# Test 4: Modify user information with invalid data
PUT http://localhost:5000/modify
Content-Type: application/json

HTTP/1.1 405

# Test 5: Delete a user with invalid email format
DELETE http://localhost:5000/delete-user/

HTTP/1.1 400

# Test 6: Add permissions with missing fields
POST http://localhost:5000/add-permissions
Content-Type: application/json


  # Missing "write", "read", and "admin" fields

HTTP/1.1 400

# Test 7: Modify permissions with invalid data
PUT http://localhost:5000/modify-permissions
Content-Type: application/json

HTTP/1.1 400

# Test 8: Delete permissions with missing parameters
DELETE http://localhost:5000/delete-permissions

HTTP/1.1 400

# Test 9: Retrieve permissions by project with invalid project ID
GET http://localhost:5000/permissions-by-project/

HTTP/1.1 409

# Test 10: Retrieve permissions by email with invalid email format
GET http://localhost:5000/permissions-by-email/

HTTP/1.1 409
