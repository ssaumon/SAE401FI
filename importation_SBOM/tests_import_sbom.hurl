GET http://localhost:5000/sbom
HTTP 200

POST http://localhost:5000/sbom
{
    "bomFormat": "CycloneDX",
    "specVersion": "1.4",
    "serialNumber": "urn:uuid:3e016e55-f35b-41cd-b660-e6e642ecc9e5",
    "version": 1,
    "metadata": {
        "timestamp": "2023-10-01T12:00:00Z",
        "tools": [
            {
                "vendor": "CycloneDX",
                "name": "CycloneDX Core Library",
                "version": "1.4"
            }
        ],
        "component": {
            "type": "application",
            "name": "ExampleApp",
            "version": "1.0.0",
            "swid": {
                "tagId": "ExampleApp"
            }
        }
    },
    "components": [
        {
            "type": "library",
            "name": "log4j",
            "version": "2.14.1",
            "swid": {
                "tagId": "log4j"
            },
            "purl": "pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1"
        },
        {
            "type": "library",
            "name": "jackson-databind",
            "version": "2.12.3",
            "swid": {
                "tagId": "jackson-databind"
            },
            "purl": "pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.12.3"
        }
    ]
}
HTTP 200

POST http://localhost:5000/sbom/dependance/2
{
    "type": "library",
    "name": "log4j",
    "version": "2.14.1",
    "swid": {
        "tagId": "log4j"
    },
    "purl": "pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1"
}
HTTP 200

POST http://localhost:5000/sbom/dependance/98623547
{
    "type": "library",
    "name": "log4j",
    "version": "2.14.1",
    "swid": {
        "tagId": "log4j"
    },
    "purl": "pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1"
}
HTTP 404

GET http://localhost:5000/sbom/2/ertghfrezfrg/Bonjour
HTTP 404

GET http://localhost:5000/sbom/98623547/bomFormat/Bonjour
HTTP 404

GET http://localhost:5000/sbom/2/bomFormat/Bonjour
HTTP 200

GET http://localhost:5000/sbom/dependance/delete/2/98623547
HTTP 404

GET http://localhost:5000/sbom/dependance/delete/98623547/2
HTTP 404

GET http://localhost:5000/sbom/dependance/delete/2/2
HTTP 200

GET http://localhost:5000/sbom/delete/98623547
HTTP 404

GET http://localhost:5000/sbom/delete/2
HTTP 200