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