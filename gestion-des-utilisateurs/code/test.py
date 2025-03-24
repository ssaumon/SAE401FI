def get_permissions_by_project(json_perm, project_id: str):
    return [perm for perm in json_perm if str(perm['project_id']) == str(project_id)]

# Exemple d'utilisation :
permissions = [
    {
        "project_id": "1",
        "email": "john.doe@example.com",
        "write": True,
        "read": True,
        "admin": False
    },
    {
        "project_id": "2",
        "email": "john.doe2@example.com",
        "write": True,
        "read": True,
        "admin": False
    },
    {
        "project_id": "1",
        "email": "john.doe@example.com",
        "write": True,
        "read": True,
        "admin": False
    },
    {
        "project_id": "2",
        "email": "john.doe2@example.com",
        "write": True,
        "read": True,
        "admin": False
    }
]

filtered_permissions = get_permissions_by_project(permissions, "4")
print(filtered_permissions)
