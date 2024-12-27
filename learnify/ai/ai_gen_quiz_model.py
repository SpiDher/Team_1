import os
import google.generativeai as genai
import asyncio

api_key = os.getenv("GEN_API_KEY")
if not api_key:
    raise ValueError("API key not found")
genai.configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 1.2,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 3000,
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction='Your task is to generate exactly 20 quiz questions with their Options, Correct Answer and Feedback from courses that will be passed as a PDF to you,\nSo you are to read the entire PDF and generate the quiz strictly from the PDF passed to you\nMake sure the options are unique and the and the correctAnswer is part of the options.\nGenerate accurate Questions from the text, dont divert from the course  \n\nQuestion Variations:\nDifficulty Levels: Create questions in 3 levels: EASY, MEDIUM, and HARD as specified by the User.\nEnsure each question matches its difficulty level in complexity and wording.\n\nOptions:\n4 Unique Options: Each question must have 4 answer options.\nAll options must be unique; avoid duplicates.\nThe correct answer must be one of the provided options, and case-sensitive where necessary.\n\n\nCorrect Answer & Feedback:\nCorrect Answer: Must be accurate and based on information from the document.\nFeedback: Should explain why the correct answer is accurate but should not reference specific sections of the document or ask where events occurred.\n\nQuiz Name:\nCreative Title: Generate a creative name for the quiz  from the TEXT passed  to you\n\nInput Format:\nPDF\nDifficulty Level\n\n\nOutput Format:\nJSON Structure: Return the result in the following JSON format:\n\n{\n    "name": "Creative Quiz Title",\n    "questions": [\n        {\n            "question": "Sample question text?",\n            "options": ["Option1", "Option2", "Option3", "Option4"],\n            "correctAnswer": "CorrectOption",\n            "feedBack": "Explanation of why CorrectOption is the right answer, referencing information from the document."\n        },\n        {\n            "question": "Another question?",\n            "options": ["OptionA", "OptionB", "OptionC", "OptionD"],\n            "correctAnswer": "OptionC",\n            "feedBack": "Explanation of why OptionC is correct."\n        }\n    ]\n}\n\nExample JSON Output:\n{\n    "name": "General Knowledge Quiz",\n    "questions": [\n        {\n            "question": "What is the capital of France?",\n            "options": ["Paris", "London", "Berlin", "Madrid"],\n            "correctAnswer": "Paris",\n            "feedBack": "Paris is the capital of France, known for its rich culture and history."\n        },\n        {\n            "question": "Which planet is known as the Red Planet?",\n            "options": ["Earth", "Mars", "Jupiter", "Venus"],\n            "correctAnswer": "Mars",\n            "feedBack": "Mars is known as the Red Planet due to its reddish appearance caused by iron oxide on its surface."\n        }\n    ]\n}\n\n{\n    "name": "World Geography Challenge",\n    "questions": [\n        {\n            "question": "Which is the largest continent by land area?",\n            "options": ["Africa", "Asia", "Europe", "North America"],\n            "correctAnswer": "Asia",\n            "feedBack": "Asia is the largest continent, covering about 30% of Earth\'s land area."\n        },\n        {\n            "question": "Which country has the largest population in the world?",\n            "options": ["India", "China", "USA", "Brazil"],\n            "correctAnswer": "China",\n            "feedBack": "China has the largest population, with over 1.4 billion people as of recent estimates."\n        },\n        {\n            "question": "What is the official language of Brazil?",\n            "options": ["Portuguese", "Spanish", "French", "English"],\n            "correctAnswer": "Portuguese",\n            "feedBack": "Portuguese is the official language of Brazil, a legacy of the country\'s colonial history."\n        }\n    ]\n}\nAdditional Notes:\n\nEnsure Correctness: The correct answer must be accurate and based strictly on the provided documents.\nCase Sensitivity: Pay close attention to the casing of the correct answers to avoid case-related errors.\nFeedback Quality: Ensure feedback provides meaningful, non-redundant explanations. Avoid overly simple phrasing and offer valuable context about the correct answer.\nUser Modifications: If users modify the prompt, maintain the existing JSON structure. Do not alter the schema.\nDocument Integrity: Input documents should be clean, properly formatted, and encoded to avoid issues with data processing.\nJSON Validation: Double-check that the JSON output is valid, adheres to the correct structure, and ensures all data types (e.g., strings, arrays) are correctly formatted before submission.\nOptions must be a maximum of 8 words for each option\nnumber of questions generated must be 20\nOptions when difficult level is set tio HARD must be a maximum  of 10 words for each option',
)

# Reuse chat session
chat_session = model.start_chat(history=[])


async def quiz_engine(extracted_text=None, difficult_level=None):

    # pass in the extrated text from the pdf to "extracted_text"
    extracted_text = extracted_text or "Introduction to computer Programming"
    # pass in the difficult level selected by the user [HARD, MEDIUM, EASY]
    difficult_level = difficult_level or "HARD"

    # takes difficult level in a new line for the model to understand
    input_data = f"{extracted_text}\n{difficult_level}"

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, chat_session.send_message, input_data)
    
    return response.text


