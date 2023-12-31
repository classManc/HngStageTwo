## HngStageTwo
A Restful API that can perfom CRUD operations an a Person resource.

# API Endpoints

### Endpoint 1: Create a Person

- **Description:** This endpoint allows you to add a new person to the database.
- **URL:** `/api/person`
- **HTTP Method:** POST

**Request Format:**
```json
{
  "name": "John Doe",  // Required field. Should be a string and cannot be blank.
}
```

**Response Format (Success - Status Code: 201):**

```json
{
  "id": 1,
  "name": "John Doe",
}
```

**Response Format (Error(if you provide an integer or any other datatype as a value for the mame field other than a string(alphabet))(- Status Code: 400)):**

```json
{
  "name":"Only alphabetic characters are allowed in the name field.",
}
```

**Response Format (Error(if you provide an existing name)(- Status Code: 400)):**

```json
{
  "name":"person with this name already exists.",
}
```


### Endpoint 2: Get a Person by ID

- **Description:** This endpoint allows you to retrieve a person's information by their ID.
- **URL:** `/api/{id}`
- **HTTP Method:** GET

**Request Parameters:**

- `id` (integer): The ID of the person to retrieve. Required.

**Response Format (Success - Status Code: 200):**

```json
{
  "id": 1,           // The ID of the person.
  "name": "John Doe" // The name of the person.
}
```

**Response Format (Error(if you provide a non-existent id)(- Status Code: 404)):**

```json
{
  "detail":"Not Found",
}
```



### Endpoint 3: Update a Person by ID

- **Description:** This endpoint allows you to update a person's information by their ID.
- **URL:** `/api/{id}`
- **HTTP Method:** PUT

**Request Parameters:**

- `id` (integer): The ID of the person to update. Required.
  
**Request Format:**

```json
{
  "name": "New Name"  // The new name for the person. Required field. Should be a string and cannot be blank.
}
```
**Response Format (Success - Status Code: 200):**

```json
{
  "id": 1,           // The ID of the updated person.
  "name": "New Name" // The updated name of the person.
}
```

**Response Format (Error(if you provide a non-existent id)(- Status Code: 404)):**

```json
{
  "detail":"Not Found",
}
```
**Response Format (Error(if you provide an integer or any other datatype as a value for the mame field other than a string(alphabet))(- Status Code: 400)):**

```json
{
  "name":"Only alphabetic characters are allowed in the name field.",
}
```

**Response Format (Error(if you provide an existing name)(- Status Code: 400)):**

```json
{
  "name":"person with this name already exists.",
}
```



### Endpoint 4: Patch a Person by ID

- **Description:** This endpoint allows you to partially update a person's information by their ID.
- **URL:** `/api/{id}`
- **HTTP Method:** PATCH

**Request Parameters:**

- `id` (integer): The ID of the person to patch. Required.
  
**Request Format:**

```json
{
  "name": "New Name"  // The new name for the person. Required field. Should be a string and cannot be blank.
}
```
**Response Format (Success - Status Code: 200):**

```json
{
  "id": 1,           // The  ID of the updated person.
  "name": "New Name" // The updated name of the person.
}
```

**Response Format (Error(if you provide a non-existent id)(- Status Code: 404)):**

```json
{
  "detail":"Not Found",
}
```
**Response Format (Error(if you provide an integer or any other datatype as a value for the mame field other than a string(alphabet))(- Status Code: 400)):**

```json
{
  "name":"Only alphabetic characters are allowed in the name field.",
}
```

**Response Format (Error(if you provide an existing name)(- Status Code: 400)):**

```json
{
  "name":"person with this name already exists.",
}
```


### Endpoint 5: Delete a Person by ID

- **Description:** This endpoint allows you to delete a person's information by their ID.
- **URL:** `/api/person/{id}`
- **HTTP Method:** DELETE

**Request Parameters:**

- `id` (integer): The ID of the person to delete. Required.

**Response Format (Success - Status Code: 204):**

The response for this endpoint does not include a JSON body. Upon successful deletion, it returns a status code of 204 (No Content).

**Response Format (Error(if you provide a non-existent id)(- Status Code: 404)):**

```json
{
  "detail":"Not Found",
}
```









