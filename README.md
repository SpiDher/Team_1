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

## **1. Generate Quiz (`/gen_quiz/`)**

### Description
This endpoint accepts a POST request with the text and level to generate a quiz. The request should contain the `level` and `text` fields. The level could be values like "beginner", "intermediate", or "advanced". The `text` should be the content from which quiz questions are generated.

### Request Method: `POST`

### Request Body
```json
{
    "level": "beginner",  // Example level (can be "beginner", "intermediate", etc.)
    "text": "This is a sample text to generate quiz questions from."  // Sample text for quiz generation
}
```

### Example Usage (JavaScript)

```javascript
fetch('/gen_quiz/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        level: 'beginner',  // Example level (can be "beginner", "intermediate", etc.)
        text: 'This is a sample text to generate quiz questions from.'  // Sample text for quiz generation
    })
})
.then(response => response.json())
.then(data => console.log('Quiz generated:', data.quiz))
.catch(error => console.error('Error:', error));
```

---

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