# Python RESTful API

This API allows dynamic querying, insertion, and updating of records across multiple database tables based on the request payload. By specifying the table name and relevant data in the payload, users can interact with specific tables using a single endpoint.

## Requirements

- Python 3.12
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/m1guel17/python_RESTful_API.git
   cd python_RESTful_API
   ```

2. Install the required Python packages:
   ```py
   pip install -r requirements.txt

3. Set up your database configuration in the config.py file.
   ```python
   class Config:
      SECRET_KEY = os.environ.get('SECRET_KEY') or "S3CR37"
      SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///DATABASE.db')
      SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```

4. Run the application:
   ```bash
   python3.12 run.py
   ```

    The API will be available at http://127.0.0.1:80/

## Endpoints

### **GET**
#### Request Payload Examples:
For this example we'll request the instance(s) from a specific Table
<table>
<tr>
<th align="center" padding="0" width=441px>
<p><small>No filters field</small></p>
</th>
<th align="center" padding="0" width=441px>
<p><small>With filters api will return all instances that match filter</small></p>
</th>
</tr>
<tr>
<td style="padding: 0px;">
  
```jsonc
{
  "table": "ClientModel"
}

// Api will return all instances from Table 

  
```
</td> <td style="padding: 0px;">

```jsonc
{
    "table": "ClientModel",
    "filters": {
        "email": "johndoe@example.com",
        "lastName": "Doe"
    }
}
```
</td>
</tr>
</table>

### Response Payload Examples:

<table>
<tr>
<th align="center" padding="0" width=400px>
<p><small>All instances from Table</small></p>
</th>
<th align="center" padding="0" width=400px>
<p><small>All instances that match filter</small></p>
</th>
</tr>
<tr>
<td style="padding: 0px;">
 
```jsonc
[
    {
        "cellphone": "1234567890",
        "createdAt": "Sun, 10 Nov 2024 01:07:40 GMT",
        "createdBy": "admin",
        "email": "johndoe@example.com",
        "firstName": "John",
        "id": 1,
        "lastName": "Doe",
        "modifiedBy": "admin",
        "modifiedOn": "Sun, 10 Nov 2024 01:07:40 GMT"
    },
    {
        "cellphone": "15236585585",
        "createdAt": "Sun, 10 Nov 2024 01:09:05 GMT",
        "createdBy": "admin",
        "email": "somebody@example.com",
        "firstName": "Sam",
        "id": 2,
        "lastName": "Somebody",
        "modifiedBy": "admin",
        "modifiedOn": "Sun, 10 Nov 2024 01:09:05 GMT"
    },
    ...
]
```
</td> <td style="padding: 0px;">

```jsonc
[
    {
        "cellphone": "1234567890",
        "createdAt": "Sun, 10 Nov 2024 01:07:40 GMT",
        "createdBy": "admin",
        "email": "johndoe@example.com",
        "firstName": "John",
        "id": 1,
        "lastName": "Doe",
        "modifiedBy": "admin",
        "modifiedOn": "Sun, 10 Nov 2024 01:07:40 GMT"
    }
]












``` 
</td>
</tr>
</table>

### **POST**
#### Insert Payload Example:
For this example we'll Insert data into a specified table
```jsonc
{
    "table": "ClientModel",
    "data": {
        "firstName": "John",
        "lastName": "Doe",
        "email": "johndoe@example.com",
        "cellphone": "15236585585",
        "createdBy": "admin",
        "modifiedBy": "admin"
    }
}
```

### Response Payload Example:
```jsonc
{
    "id": 1,
    "message": "Record inserted successfully"
}
// This will return a 201 Status Code
``` 
In case of sending duplicate values to unique values column the following error will prompt:


## Error Handling
Each endpoint will return an error message with a status code for invalid input, missing records, or issues with database operations.
1. 400 Bad Request: For issues like invalid table names, missing fields, or invalid data in the request payload.
2. 409 Conflict: The request could not be processed because of conflict in the request.