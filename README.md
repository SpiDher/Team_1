# SEN PROJECT FOR GROUP 1 🚀



# Django Course Content and Quiz API

This Django project provides an API to extract course content from a JSON file (`cos.json`), generate quizzes based on extracted text, and serve downloadable course materials. It uses a custom utility class to handle file extraction, OCR, and quiz generation.

## Features

- **Course Content**: Fetches course content from a JSON file (`cos.json`) and returns it in a structured format.
- **Quiz Generation**: Accepts a file (e.g., PDF), processes the content, and generates quizzes based on the extracted text.
- **Topic Material Download**: Allows downloading course material (PDF files) via a file path.
  
## Project Structure

```
Backend/
│
├── Backend/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
│   └── cos.json   # JSON file containing course content
│
├── learnify/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py   # API views for handling requests
│   ├── utils.py   # Utility functions for text extraction
│   └── ai/
│       └── use_ai_gen_quiz.py  # AI logic for quiz generation
│
└── manage.py
```

Here is the full documentation with the requested details:

---

# Backend API Documentation

This backend API is designed for quiz generation, file retrieval, and course content handling. Below are the available endpoints and how to interact with them using JavaScript.

## Available Endpoints

1. **`/gen_quiz/`** – Generate a quiz based on provided text and level.
2. **`/content/`** – Retrieve the course content.
3. **`/materials/`** – Retrieve a downloadable material file.

---



### 1. `/gen_quiz/` - Generate Quiz

This endpoint generates a quiz from either a file or a text description.

#### Method: `POST`

#### Request Body (JSON format):

- **`file`** *(optional)*: The file to process (a PDF or image) to generate quiz questions. This can be uploaded using `multipart/form-data`.
- **`level`** *(optional)*: The difficulty level of the quiz. Possible values can be `"beginner"`, `"intermediate"`, `"advanced"`.
- **`quiz-desc`** *(optional)*: A custom description (text) to generate quiz questions from. If this is provided, the system will generate the quiz from the description instead of the file.

#### Example Request (with file):

```bash
POST /gen_quiz/
Content-Type: multipart/form-data

{
    "file": <file>,  # A PDF or image file uploaded
    "level": "beginner",
    "quiz-desc": "A sample description for quiz generation"
}
```

#### Example Request (with description only):

```bash
POST /gen_quiz/
Content-Type: application/json

{
    "quiz-desc": "This is a sample text to generate quiz questions from.",
    "level": "beginner"
}
```

#### Example Request (with no file or description):

```bash
POST /gen_quiz/
Content-Type: application/json

{
    "level": "intermediate"
}
```

#### Example Response:

```json
{
    "quiz": [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Rome"],
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5"],
            "answer": "4"
        }
    ]
}
```

#### Notes:

- The file is **optional**. If no file is uploaded, the system will generate the quiz based on the provided description.
- If neither a file nor description is provided, the system will return an error.

---

### 2. `/materials/` - Download Material

This endpoint allows you to download a material (such as a PDF).

#### Method: `GET`

#### Request Parameters:

- **`filename`** *(required)*: The name of the file you want to download. Example: `pdf-test.pdf`.

#### Example Request:

```bash
GET /materials/?filename=pdf-test.pdf
```

#### Example Response:

The file will be returned as a downloadable attachment.

---

## Error Responses

### 1. Missing File or Description in `/gen_quiz/`:

If neither a file nor description is provided, the API will return a 400 error:

```json
{
    "error": "No file or description provided"
}
```

### 2. Invalid Request Method:

If the wrong HTTP method is used, the API will return a 400 error:

```json
{
    "error": "Invalid request method"
}
```

---

## Example Usage

### Using JavaScript Fetch to Send Data to `/gen_quiz/`

You can send a POST request to the `/gen_quiz/` endpoint using JavaScript's `fetch` API. Here's an example that sends a description instead of a file:

```javascript
fetch('/gen_quiz/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        level: 'beginner',  // Example level (can be "beginner", "intermediate", etc.)
        quiz-desc: 'This is a sample text to generate quiz questions from.'  // Sample text for quiz generation
    })
})
.then(response => response.json())
.then(data => {
    console.log(data);  // Handle the quiz data
})
.catch(error => {
    console.error('Error:', error);  // Handle errors
});
```

### Handling File Upload with JavaScript

If you'd like to upload a file instead of sending a description, you can use the `FormData` API:

```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);
formData.append('level', 'beginner');  // Optional level
formData.append('quiz-desc', '');  // Optional description (empty string if not used)

fetch('/gen_quiz/', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => {
    console.log(data);  // Handle the quiz data
})
.catch(error => {
    console.error('Error:', error);  // Handle errors
});
```

---

## Conclusion

This API provides a flexible way to generate quizzes from either a file or a description, making it easy to integrate quiz generation into any application. Whether you're uploading a file or sending a description, the system will process your request and return a quiz based on the provided content.



## **2. Retrieve Course Content (`/content/`)**

### Description
This endpoint retrieves the course content from a pre-defined JSON file. The response will contain the course data, which includes topics and descriptions.

### Request Method: `GET`

### Example Usage (JavaScript)

```javascript
fetch('/content/', {
    method: 'GET',
})
.then(response => response.json())
.then(data => console.log('Course Content:', data.course_data))
.catch(error => console.error('Error:', error));
```

---

## **3. Retrieve Material File (`/materials/`)**

### Description
This endpoint allows you to download a material file. You need to provide the `filename` of the material you want to download via the query parameter. The server will return the file as an attachment.

### Request Method: `GET`

### Query Parameter
- `filename`: The name of the file to be downloaded (e.g., `pdf-test.pdf`).

### Example Usage (JavaScript)

```javascript
fetch('/materials/?filename=pdf-test.pdf', {
    method: 'GET',
})

```

---

## Response Format

All endpoints return responses in JSON format. Below are examples of successful responses for each endpoint:

### **Response from `/gen_quiz/`**

```json
{
    "quiz": [
        {
            "question": "What is Computer Organization and Systems?",
            "options": [
                "A subject in computer science",
                "A programming language",
                "An operating system",
                "A hardware component"
            ],
            "answer": "A subject in computer science"
        },
        // More questions...
    ]
}
```

### **Response from `/content/`**

```json
{
    "course_data": {
        "Introduction To COS111": "### Introduction to COS (Computer Organization and Systems)...",
        "Programming with vb": "blah blah",
        // More topics...
    }
}
```

### **Response from `/materials/`**

File content will be sent as a binary response, allowing you to download it. If the file does not exist, the following error response will be returned:

```json
{
    "error": "file not found"
}
```

---

## Error Handling

- If any of the required fields (like `level` or `text`) are missing in the `/gen_quiz/` request, or if the file is not found in the `/materials/` endpoint, an error message will be returned as shown in the responses above.
- For all other errors, a generic `500 Internal Server Error` is returned.

---

## Summary

- **POST** `/gen_quiz/`: Generate a quiz based on text input.
- **GET** `/content/`: Retrieve the course content.
- **GET** `/materials/`: Retrieve downloadable material using a filename.

---

This document provides detailed instructions on how to interact with the backend API via JavaScript fetch requests.