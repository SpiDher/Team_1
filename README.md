# **API Documentation: Backend**

This README provides an overview of the available API endpoints, their functionality, and how to interact with them. It is tailored for intermediate frontend developers.

---

## **Base URL**
The base URL for all endpoints is:

```
http://<server-domain>/api/
```

---

## **Endpoints**

### 1. **Home**
- **URL**: `/api/`
- **Method**: `GET`
- **Description**: A simple welcome endpoint to check the API status.
- **Response**:
  ```plaintext
  Welcome
  ```

---

### 2. **Generate Quiz**
- **URL**: `/api/quiz/`
- **Method**: `POST` or `GET`
- **Description**: Generates a quiz based on either uploaded content or a text description.
- **Request Parameters**:
  - **`file`** (optional): A file to process (PDF or similar).
  - **`content`** (optional): A string description (max length: 25,000 characters).
  - **`level`** (required): The difficulty level (e.g., `easy`, `medium`, `hard`).
- **Response**:
  - **Success**: Returns the generated quiz in JSON format.
  - **Error**: 
    ```json
    {"error": "No File or Content provided"}
    ```

---

### 3. **Fetch Course Content**
- **URL**: `/api/content/`
- **Method**: `GET`
- **Description**: Retrieves course data in JSON format for frontend display.
- **Response**: 
  ```json
  {
    "topic_1": {"content": "<h3>Introduction</h3><p>...</p>"},
    "topic_2": {"content": "<h3>Advanced Concepts</h3><p>...</p>"}
  }
  ```

---

### 4. **Download Topic Material**
- **URL**: `/api/materials/`
- **Method**: `GET`
- **Description**: Downloads a file (e.g., lecture notes or supplementary material) from the backend.
- **Request Parameters**:
  - **`filename`** (required): The name of the file to download.
- **Response**:
  - **Success**: Returns the file as an attachment.
  - **Error**: 
    ```json
    {"error": "file not found"}
    ```

---

### 5. **Generate Random Quiz**
- **URL**: `/api/ran_quiz/`
- **Method**: `GET`
- **Description**: Randomly selects a file and generates a quiz based on its content.
- **Request Parameters**:
  - **`level`** (optional): The difficulty level.
- **Response**: Returns the generated quiz in JSON format.

---

### 6. **List Available Files**
- **URL**: `/api/list/`
- **Method**: `GET`
- **Description**: Lists all available files stored on the server.
- **Response**:
  ```json
  {"Materials": ["file1.pdf", "file2.docx", "file3.txt"]}
  ```

---

## **How to Use**

### **Making Requests**
- Use `fetch`, `Axios`, or any HTTP client to interact with these endpoints.
- Ensure to send the correct headers and data format (e.g., multipart form-data for file uploads).

### **Example: Generate Quiz**
#### Using `fetch`:
```javascript
const formData = new FormData();
formData.append("file", fileInput.files[0]);
formData.append("level", "medium");

fetch("http://<server-domain>/api/quiz/", {
  method: "POST",
  body: formData,
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));
```

---

## **Error Handling**
- Always handle error responses gracefully.
- Common errors include:
  - Missing required parameters.
  - File not found for downloads.
  - Backend exceptions (e.g., read-only filesystem in production).

---

## **Notes for Integration**
- Ensure `level` values are standardized (e.g., `easy`, `medium`, `hard`).
- Verify filenames before requesting `/api/materials/` to avoid errors.
- `/api/quiz/` supports both file-based and text-based input; choose appropriately based on user input.

```markdown
# **API Documentation: Backend**

This README provides an overview of the available API endpoints, their functionality, and how to interact with them. It is tailored for intermediate frontend developers.

---

## **Base URL**
The base URL for all endpoints is:

```
http://<server-domain>/api/
```

---

## **Endpoints and Example Fetch Requests**

### 1. **Home**
- **URL**: `/api/`
- **Method**: `GET`
- **Description**: A simple welcome endpoint to check the API status.
- **Response**:
  ```plaintext
  Welcome
  ```
- **Fetch Request**:
  ```javascript
  fetch("http://<server-domain>/api/")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
  ```

---

### 2. **Generate Quiz**
- **URL**: `/api/quiz/`
- **Method**: `POST` or `GET`
- **Description**: Generates a quiz based on either uploaded content or a text description.
- **Request Parameters**:
  - **`file`** (optional): A file to process (PDF or similar).
  - **`content`** (optional): A string description (max length: 25,000 characters).
  - **`level`** (required): The difficulty level (e.g., `easy`, `medium`, `hard`).
- **Response**:
  - **Success**: Returns the generated quiz in JSON format.
  - **Error**: 
    ```json
    {"error": "No File or Content provided"}
    ```
- **Fetch Request**:
  ```javascript
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  formData.append("level", "medium");

  fetch("http://<server-domain>/api/quiz/", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
  ```

---

### 3. **Fetch Course Content**
- **URL**: `/api/content/`
- **Method**: `GET`
- **Description**: Retrieves course data in JSON format for frontend display.
- **Response**:
  ```json
  {
    "topic_1": {"content": "<h3>Introduction</h3><p>...</p>"},
    "topic_2": {"content": "<h3>Advanced Concepts</h3><p>...</p>"}
  }
  ```
- **Fetch Request**:
  ```javascript
  fetch("http://<server-domain>/api/content/")
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
  ```

---

### 4. **Download Topic Material**
- **URL**: `/api/materials/`
- **Method**: `GET`
- **Description**: Downloads a file (e.g., lecture notes or supplementary material) from the backend.
- **Request Parameters**:
  - **`filename`** (required): The name of the file to download.
- **Response**:
  - **Success**: Returns the file as an attachment.
  - **Error**: 
    ```json
    {"error": "file not found"}
    ```
- **Fetch Request**:
  ```javascript
  const filename = "lecture_notes.pdf";
  fetch(`http://<server-domain>/api/materials/?filename=${filename}`)
    .then((response) => {
      if (response.ok) {
        return response.blob();
      } else {
        throw new Error("File not found");
      }
    })
    .then((blob) => {
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
    })
    .catch((error) => console.error("Error:", error));
  ```

---

### 5. **Generate Random Quiz**
- **URL**: `/api/ran_quiz/`
- **Method**: `GET`
- **Description**: Randomly selects a file and generates a quiz based on its content.
- **Request Parameters**:
  - **`level`** (optional): The difficulty level.
- **Response**: Returns the generated quiz in JSON format.
- **Fetch Request**:
  ```javascript
  const level = "medium";
  fetch(`http://<server-domain>/api/ran_quiz/?level=${level}`)
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
  ```

---

### 6. **List Available Files**
- **URL**: `/api/list/`
- **Method**: `GET`
- **Description**: Lists all available files stored on the server.
- **Response**:
  ```json
  {"Materials": ["file1.pdf", "file2.docx", "file3.txt"]}
  ```
- **Fetch Request**:
  ```javascript
  fetch("http://<server-domain>/api/list/")
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
  ```

---

## **How to Use**

### **Making Requests**
- Use `fetch`, `Axios`, or any HTTP client to interact with these endpoints.
- Ensure to send the correct headers and data format (e.g., multipart form-data for file uploads).

---

## **Error Handling**
- Always handle error responses gracefully.
- Common errors include:
  - Missing required parameters.
  - File not found for downloads.
  - Backend exceptions (e.g., read-only filesystem in production).

---

## **Notes for Integration**
- Ensure `level` values are standardized (e.g., `easy`, `medium`, `hard`).
- Verify filenames before requesting `/api/materials/` to avoid errors.
- `/api/quiz/` supports both file-based and text-based input; choose appropriately based on user input.

