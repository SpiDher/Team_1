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

# API Documentation

## Overview
This document provides a comprehensive overview of the API endpoints available in the project. Each endpoint is described with its method, purpose, input parameters, and expected responses.

---

## Endpoints

### 1. `GET /`
- **Description**: Returns a welcome message.
- **Response**:
  - **Status**: 200
  - **Body**: Plain text message: `Welcome`
  async function generateQuiz(file, level, desc) {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('level', level);
  formData.append('quiz-desc', desc);

  try {
    const response = await fetch('/api/quiz/', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const data = await response.json();
      console.log('Quiz:', data.quiz);
    } else {
      console.error('Failed to generate quiz:', await response.json());
    }
  } catch (error) {
    console.error('Error:', error);
  }
}


---

### 2. `POST /api/quiz/`
- **Description**: Generates a quiz based on a provided file or description.
- **Request**:
  - **Method**: POST
  - **Headers**: `Content-Type: multipart/form-data`
  - **Parameters**:
    - `file` (optional, file): A file containing content to generate a quiz.
    - `level` (optional, string): Difficulty level of the quiz.
    - `quiz-desc` (optional, string): Description of the quiz if no file is provided.
- **Response**:
  - **Status**: 200
  - **Body**:
    ```json
    {
      "quiz": {
        "name": "Quiz Title",
        "questions": [...]
      }
    }
    ```
  - **Error Response**:
    - **Status**: 400
    - **Body**:
      ```json
      {
        "error": "No file provided"
      }
      ```
      async function fetchContent() {
  try {
    const response = await fetch('/api/content/');

    if (response.ok) {
      const data = await response.json();
      console.log('Course Content:', data.course_data);
    } else {
      console.error('Failed to fetch content:', await response.json());
    }
  } catch (error) {
    console.error('Error:', error);
  }
}


---

### 3. `GET /api/content/`
- **Description**: Retrieves course data from the backend.
- **Request**:
  - **Method**: GET
- **Response**:
  - **Status**: 200
  - **Body**:
    ```json
    {
      "course_data": { ... }
    }
    ```
    async function downloadMaterial(filename) {
  try {
    const response = await fetch(`/api/materials/?filename=${filename}`);

    if (response.ok) {
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = filename;
      document.body.appendChild(link);
      link.click();
      link.remove();
    } else {
      console.error('Failed to download material:', await response.json());
    }
  } catch (error) {
    console.error('Error:', error);
  }
}


---

### 4. `GET /api/materials/`
- **Description**: Retrieves a specific topic material file.
- **Request**:
  - **Method**: GET
  - **Parameters**:
    - `filename` (string): Name of the file to retrieve.
- **Response**:
  - **Status**: 200 (if file exists)
  - **Headers**: `Content-Disposition: attachment; filename="<filename>"`
  - **Body**: File content as a binary stream.
  - **Error Response**:
    - **Status**: 400
    - **Body**:
      ```json
      {
        "error": "file not found"
      }
      ```
      async function generateRandomQuiz(level) {
  try {
    const response = await fetch(`/api/ran_quiz/?level=${level}`);

    if (response.ok) {
      const data = await response.json();
      console.log('Random Quiz:', data.quiz);
    } else {
      console.error('Failed to fetch random quiz:', await response.json());
    }
  } catch (error) {
    console.error('Error:', error);
  }
}


---

### 5. `GET /api/ran_quiz/`
- **Description**: Generates a quiz based on a randomly selected file.
- **Request**:
  - **Method**: GET
  - **Parameters**:
    - `level` (optional, string): Difficulty level of the quiz.
- **Response**:
  - **Status**: 200
  - **Body**:
    ```json
    {
      "quiz": {
        "name": "Quiz Title",
        "questions": [...]
      }
    }
    ```
    async function listFiles() {
  try {
    const response = await fetch('/api/list/');

    if (response.ok) {
      const data = await response.json();
      console.log('File List:', data.Materials);
    } else {
      console.error('Failed to fetch file list:', await response.json());
    }
  } catch (error) {
    console.error('Error:', error);
  }
}


---

### 6. `GET /api/list/`
- **Description**: Returns a list of all available materials in the media directory.
- **Request**:
  - **Method**: GET
- **Response**:
  - **Status**: 200
  - **Body**:
    ```json
    {
      "Materials": ["file1.pdf", "file2.docx", ...]
    }
    ```
    async function listFiles() {
  try {
    const response = await fetch('/api/list/');

    if (response.ok) {
      const data = await response.json();
      console.log('File List:', data.Materials);
    } else {
      console.error('Failed to fetch file list:', await response.json());
    }
  } catch (error) {
    console.error('Error:', error);
  }
}



# Documentation for Backend JSON Response

## Overview
This document describes the structure and content of the JSON object returned by the backend for a functional programming quiz. The JSON provides all the necessary information for rendering a quiz in a frontend application, including questions, options, correct answers, and feedback.

## JSON Structure

### Root Object
- **`quiz`**: Contains the quiz data as a JSON string. The content is formatted as a nested JSON object with quiz details.

### Nested Structure
#### **Quiz Details**
- **`name`** *(string)*: The title of the quiz.

#### **Questions**
- **`questions`** *(array)*: A list of quiz questions. Each question object includes details such as the question text, multiple-choice options, the correct answer, and feedback.

#### **Question Object**
Each question object contains the following fields:

1. **`question`** *(string)*:
   - The text of the question being asked.

2. **`options`** *(array of strings)*:
   - A list of possible answers. Each option is represented as a string.

3. **`correctAnswer`** *(string)*:
   - The correct answer to the question. This value should match one of the strings in the `options` array.

4. **`feedBack`** *(string)*:
   - Additional explanation or clarification provided after the user answers the question.

## Example JSON
```json
{
  "quiz": {
    "name": "COS2 Mastery Quiz",
    "questions": [
      {
        "question": "Explain the concept of 'referential transparency' in the context of functional programming and provide a specific example illustrating its benefits.",
        "options": [
          "Referential transparency means that a function's output depends only on its input, regardless of execution order. This allows for easier reasoning and optimization, but it's computationally expensive.",
          "Referential transparency is a property where the order of function execution matters. It increases code complexity but provides more efficient execution.",
          "Referential transparency means that a function's output depends only on its input, regardless of execution order. This allows for easier reasoning, optimization, and parallelization. For example, `add(2, 3)` always returns 5, regardless of when it's called.",
          "Referential transparency is primarily used for error handling. It helps prevent crashes but can reduce code readability."
        ],
        "correctAnswer": "Referential transparency means that a function's output depends only on its input, regardless of execution order. This allows for easier reasoning, optimization, and parallelization. For example, `add(2, 3)` always returns 5, regardless of when it's called.",
        "feedBack": "Referential transparency ensures that a function always produces the same output for the same input, making code easier to understand, optimize, and parallelize. The example highlights this consistent behavior."
      },
      {
        "question": "Discuss the trade-offs involved in choosing between eager and lazy evaluation strategies in functional programming. Provide scenarios where one approach would be significantly more efficient than the other.",
        "options": [
          "Eager evaluation is always faster than lazy evaluation.",
          "Lazy evaluation is always better because it avoids unnecessary computations.",
          "Eager evaluation is best for situations where all data is readily available. Lazy evaluation is more efficient when dealing with potentially infinite data streams or situations where not all results are needed.",
          "There are no significant trade-offs; both approaches are equivalent in performance."
        ],
        "correctAnswer": "Eager evaluation is best for situations where all data is readily available. Lazy evaluation is more efficient when dealing with potentially infinite data streams or situations where not all results are needed.",
        "feedBack": "The choice between eager and lazy evaluation depends heavily on the nature of the data and the required computations. Lazy evaluation excels when dealing with large or potentially infinite datasets, while eager evaluation is preferable when all data is readily available and immediate results are crucial."
      }
      // Additional questions...
    ]
  }
}
```

## Notes
1. **Data Format**:
   - Ensure all string fields are properly escaped when serializing to JSON.

2. **Validation**:
   - Verify that each `correctAnswer` matches one of the `options` for consistency.
   - Validate that `questions` is an array with at least one element.

3. **Feedback Integration**:
   - Feedback should provide meaningful insights to help the user understand the concept better.

4. **Expandability**:
   - The structure allows adding more questions and modifying existing ones with ease.

5. **Use Case**:
   - Ideal for functional programming quizzes or educational purposes requiring dynamic rendering of questions and answers.

## Backend Responsibilities
- Ensure the JSON is dynamically generated based on a database or predefined logic.
- Maintain consistency between `options` and `correctAnswer` fields.
- Provide meaningful and constructive feedback for all questions.

## Frontend Responsibilities
- Parse the JSON and render the quiz UI dynamically.
- Display feedback immediately after the user answers a question.
- Allow navigation between questions in the quiz.



This document provides detailed instructions on how to interact with the backend API via JavaScript fetch requests.