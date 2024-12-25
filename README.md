SEN Project for Group 1 🚀

Django Course Content and Quiz API

This project provides an API built with Django for extracting course content, generating quizzes, and serving downloadable course materials. It leverages custom utilities for file processing, OCR, and AI-based quiz generation.


---

Features

Course Content Extraction: Fetches course content from a JSON file (cos.json) in a structured format.

Quiz Generation: Generates quizzes based on uploaded files (e.g., PDFs) or input descriptions.

Material Download: Serves downloadable course materials (PDFs or other files).



---

Project Structure

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


---

API Documentation

1. GET /

Description: Returns a welcome message.
Response:

Welcome


---

2. POST /api/quiz/

Description: Generates a quiz based on a provided file or description.
Parameters:

file (optional): File to generate quiz content.

level (optional): Difficulty level of the quiz.

quiz-desc (optional): Quiz description if no file is provided.


Response:

Success:

{
  "quiz": {
    "name": "Quiz Title",
    "questions": [...]
  }
}

Error:

{
  "error": "No file provided"
}



---

3. GET /api/content/

Description: Retrieves course data from the backend.
Response:

{
  "course_data": { ... }
}


---

4. GET /api/materials/

Description: Downloads a specific material file.
Parameters:

filename: Name of the file to retrieve.


Response:

Success: File download.

Error:

{
  "error": "File not found"
}



---

5. GET /api/ran_quiz/

Description: Generates a quiz based on a randomly selected file.
Parameters:

level (optional): Difficulty level of the quiz.


Response:

{
  "quiz": {
    "name": "Quiz Title",
    "questions": [...]
  }
}


---

6. GET /api/list/

Description: Lists all available materials in the media directory.
Response:

{
  "Materials": ["file1.pdf", "file2.docx", ...]
}


---

Example JavaScript Usage

Generate Quiz

async function generateQuiz(file, level, desc) {
  const formData = new FormData();
  if (file) formData.append('file', file);
  if (level) formData.append('level', level);
  if (desc) formData.append('quiz-desc', desc);

  try {
    const response = await fetch('/api/quiz/', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const data = await response.json();
      console.log('Generated Quiz:', data.quiz);
    } else {
      console.error('Failed to generate quiz:', await response.json());
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

Fetch Course Content

async function fetchCourseContent() {
  try {
    const response = await fetch('/api/content/');

    if (response.ok) {
      const data = await response.json();
      console.log('Course Content:', data.course_data);
    } else {
      console.error('Failed to fetch course content:', await response.json());
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

Download Material

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

Generate Random Quiz

async function generateRandomQuiz(level) {
  try {
    const response = await fetch(`/api/ran_quiz/?level=${level}`);

    if (response.ok) {
      const data = await response.json();
      console.log('Random Quiz:', data.quiz);
    } else {
      console.error('Failed to generate random quiz:', await response.json());
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

List Materials

async function listAvailableMaterials() {
  try {
    const response = await fetch('/api/list/');

    if (response.ok) {
      const data = await response.json();
      console.log('Available Materials:', data.Materials);
    } else {
      console.error('Failed to fetch materials:', await response.json());
    }
  } catch (error) {
    console.error('Error:', error);
  }
}


---

Backend JSON Response Documentation

Overview

The backend JSON provides data for rendering quizzes dynamically, including questions, options, correct answers, and feedback.

Example JSON

{
  "quiz": {
    "name": "Sample Quiz",
    "questions": [
      {
        "question": "What is Django?",
        "options": ["A framework", "A database", "A programming language"],
        "correctAnswer": "A framework",
        "feedBack": "Django is a high-level Python web framework."
      },
      {
        "question": "Which database does Django use by default?",
        "options": ["MySQL", "SQLite", "PostgreSQL"],
        "correctAnswer": "SQLite",
        "feedBack": "Django uses SQLite as its default database."
      }
    ]
  }
}


---

Notes

1. Frontend Integration: Ensure CORS settings allow access from your frontend.


2. Validation: Validate API responses and display appropriate error messages.


3. Expandability: Add new features or endpoints by extending the views.py or utils.py modules.



This README provides complete documentation for both backend and frontend integration. Let me know if anything else needs to be added!

