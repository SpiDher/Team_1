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


# Course Data JSON Object Documentation endpoint = /api/content

## Overview
The `course_data` JSON object contains structured information about various computer science topics. It is designed to provide content and examples for educational purposes. Each topic includes detailed explanations and examples to aid in understanding the subject matter.

---

## Structure
The `course_data` object is organized as follows:

- **Key (Topic Name)**: Represents the name of the topic (e.g., "Introduction To COS111").
  - If the value is a **string**, it contains the content for the topic.
  - If the value is a **nested object**, it includes:
    - `content`: Detailed textual explanation of the topic.
    - `examples`: An array of example questions or scenarios related to the topic.

### Example Structure
```json
{
  "course_data": {
    "Topic Name": {
      "content": "Detailed description of the topic.",
      "examples": [
        "Example question or scenario 1",
        "Example question or scenario 2"
      ]
    }
  }
}
```

---

## How to Use
### Accessing Topics
To access the content of a specific topic:
```javascript
const courseData = data.course_data; // Replace 'data' with your JSON object
const topicContent = courseData["Introduction To COS111"];
console.log(topicContent); // Outputs the content as a string
```

### Accessing Nested Content
For topics with nested objects:
```javascript
const topicDetails = courseData["Concept of Computer System"];
console.log(topicDetails.content); // Outputs the detailed content
console.log(topicDetails.examples); // Outputs the examples array
```

### Iterating Through All Topics
```javascript
for (const topic in courseData) {
    if (courseData.hasOwnProperty(topic)) {
        const details = courseData[topic];
        console.log(`Topic: ${topic}`);
        if (typeof details === "object") {
            console.log("Content:", details.content);
            console.log("Examples:", details.examples);
        } else {
            console.log("Content:", details); // For string-based topics
        }
    }
}
```

---

## Example Use Case
A frontend developer can use this object to dynamically render educational content on a webpage. For instance:

1. Display all topic names as clickable links.
2. Show the `content` when a topic is selected.
3. Provide `examples` as interactive quiz questions or discussion prompts.

---

## Notes
- Ensure that all keys in the JSON object are correctly referenced.
- Use appropriate error handling to manage cases where fields like `content` or `examples` may be missing.
- For better readability, format content fields (e.g., using Markdown parsers for styled output).

---

## Future Enhancements
- Add metadata fields (e.g., difficulty level, estimated reading time) to each topic.
- Include multimedia resources (e.g., images, videos) to complement the textual content.
- Provide a search feature to quickly locate topics or concepts.







