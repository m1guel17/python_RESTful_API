# Dynamic Database API

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
- Query Data from a Table:

### Request Payload Examples:

<table>
<tr>
<th align="center" padding="0">
<img width="441" height="0px">
<p><small>Example 1</small></p>
</th>
<th align="center" padding="0">
<img width="441" height="0px">
<p><small>Example 2</small></p>
</th>
</tr>
<tr>
<td style="width: 100%; vertical-align: top; padding: 0px;">
  
```json
{
  "table": "ClientModel"
}



  
```
</td> <td style="width: 100%; vertical-align: top; padding: 0px;">

```json
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
   ```json
    [
        {
            "cellphone": "1234567890",
            "createdAt": "Sat, 09 Nov 2024 19:25:57 GMT",
            "createdBy": "admin",
            "email": "johndoe@example.com",
            "firstName": "John",
            "id": 1,
            "lastName": "Doe",
            "modifiedBy": "admin",
            "modifiedOn": "Sat, 09 Nov 2024 19:25:57 GMT"
        }
    ]
   ```  

## Error Handling
Each endpoint will return an error message with a status code for invalid input, missing records, or issues with database operations.
1. 400 Bad Request: For issues like invalid table names, missing fields, or invalid data in the request payload.
2. 409 Conflict: The request could not be processed because of conflict in the request.