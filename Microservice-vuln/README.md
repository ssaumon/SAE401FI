# Vulnerability MicroService

## Description
The **Vulnerability MicroService** is a web application built using the **Flask** library, designed to manage and manipulate information about software vulnerabilities. The service is divided into several methods, each exposed via dedicated routes on the server. This microservice allows you to perform various operations such as creating, modifying, deleting, and retrieving vulnerabilities, all through a simple HTTP interface. All data is stored in a JSON file named **Vulnerability.json**.

The application is named **Vulnerability.py** and includes a Python test script named **test.py**. An interface contract is also provided under the name **Vulnerability.yaml**.

## Routes and Methods

The application exposes several routes, each corresponding to a specific functionality. Here is an overview of the available routes:

### 1. `/`
**Method: GET**

- **Description**: Displays the "test" page to check if the microservice is functioning correctly. This route simply returns the message "Microservice Vulnerability".

### 2. `/Vulnerability`
**Methods: GET, POST, PUT**

- **GET**: Lists all the vulnerabilities stored in the database.
- **POST**: Allows you to add one or more new vulnerabilities to the database. The API can send multiple vulnerabilities simultaneously in JSON format.
- **PUT**: Allows you to modify a vulnerability without specifying an ID in the URL. This method retrieves the ID from the JSON body of the vulnerability for secure modification.

### 3. `/Vulnerability/<int:id_Vuln>`
**Methods: GET, DELETE, PUT**

- **GET**: Retrieves a specific vulnerability using its ID.
- **DELETE**: Deletes a vulnerability by specifying its ID.
- **PUT**: Modifies a vulnerability using its ID in the URL.

### 4. `/Vulnerability/sbom`
**Method: POST**

- **Description**: Allows searching for the presence of vulnerabilities in the database for a specific version of a package, sent from the SBOM (Software Bill of Materials) API. If a compromised version is found, the method returns information about that vulnerability, such as the fixed version, links to documentation, etc.

## Important Files

- **Vulnerability.py**: The main application script that defines the routes and handles requests.
- **test.py**: A Python test script to verify the proper functioning of the service and test the various routes.
- **Vulnerability.yaml**: An interface contract (Swagger/OpenAPI) that defines the routes, parameters, and possible responses.

## Example Usage

1. **Add a vulnerability** (POST method):
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{
        "VulnerabilityID": "CVE-2021-3156",
        "PkgName": "sudo",
        "InstalledVersion": "1.8.31",
        "FixedVersion": "1.9.5p2",
        "Severity": "CRITICAL",
        "Title": "Sudo - Heap-based Buffer Overflow in sudoedit (CVE-2021-3156)",
        "Description": "A heap-based buffer overflow in sudoedit in sudo before 1.9.5p2 allows privilege escalation to root via a crafted command line.",
        "References": ["https://nvd.nist.gov/vuln/detail/CVE-2021-3156"]
    }' http://127.0.0.1:5007/Vulnerability
    ```

2. **Get the list of vulnerabilities** (GET method):
    ```bash
    curl http://127.0.0.1:5007/Vulnerability
    ```

3. **Modify a vulnerability** (PUT method):
    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{
        "VulnerabilityID": "CVE-2021-3156",
        "PkgName": "sudo",
        "InstalledVersion": "1.8.31",
        "FixedVersion": "1.9.5p2",
        "Severity": "CRITICAL",
        "Title": "Sudo - Heap-based Buffer Overflow in sudoedit (CVE-2021-3156)",
        "Description": "A heap-based buffer overflow in sudoedit in sudo before 1.9.5p2 allows privilege escalation to root via a crafted command line.",
        "References": ["https://nvd.nist.gov/vuln/detail/CVE-2021-3156"]
    }' http://127.0.0.1:5007/Vulnerability
    ```

4. **Delete a vulnerability** (DELETE method):
    ```bash
    curl -X DELETE http://127.0.0.1:5007/Vulnerability/1
    ```

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/ssaumon/SAE401FI/tree/Gestion-de-vulnérabilités
    cd vulnerability-microservice
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```bash
    python Vulnerability.py
    ```

4. The application will be available at `http://127.0.0.1:5007`.

## Technologies Used

- **Flask**: A web framework for Python.
- **JSON**: The format used for storing vulnerabilities.
- **cURL**: Used in the examples to test the API routes.

## Contributors

- FI

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.
