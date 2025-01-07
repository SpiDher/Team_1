import os
import google.generativeai as genai
import asyncio
from google.ai.generativelanguage_v1beta.types import content
from absl import logging
import json

# Suppress gRPC logging
os.environ["GRPC_VERBOSITY"] = "NONE"

# Suppress absl logging
logging.set_verbosity(logging.ERROR)
logging.use_absl_handler()

api_key = os.getenv("GEM_API_KEY")
"""if not api_key:
    raise ValueError("API key not found")"""
genai.configure(api_key=api_key)

# Create the model
generation_config = {
    "temperature": 1.35,
    "top_p": 0.7,
    "top_k": 40,
    "max_output_tokens": 5000,
    "response_schema": content.Schema(
        type=content.Type.OBJECT,
        enum=[],
        required=["name", "questions"],
        properties={
            "name": content.Schema(
                type=content.Type.STRING,
            ),
            "time": content.Schema(
                type=content.Type.INTEGER,
            ),
            "questions": content.Schema(
                type=content.Type.ARRAY,
                items=content.Schema(
                    type=content.Type.OBJECT,
                    enum=[],
                    required=["question", "options", "correctAnswer", "feedBack"],
                    properties={
                        "question": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "options": content.Schema(
                            type=content.Type.ARRAY,
                            items=content.Schema(
                                type=content.Type.STRING,
                            ),
                        ),
                        "correctAnswer": content.Schema(
                            type=content.Type.STRING,
                        ),
                        "feedBack": content.Schema(
                            type=content.Type.STRING,
                        ),
                    },
                ),
            ),
        },
    ),
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction='Your task is to generate exactly 21 quiz questions with their Options, Correct Answer and Feedback from courses that will be passed as a PDF to you,\nSo you are to read the entire PDF and generate the quiz strictly from the PDF passed to you\nMake sure the options are unique and the and the correctAnswer is part of the options.\nGenerate accurate Questions from the text, dont divert from the course  \n\nQuestion Variations:\nDifficulty Levels: Create questions in 3 levels: EASY, MEDIUM, and HARD as specified by the User.\nEnsure each question matches its difficulty level in complexity and wording.\n\nOptions:\n4 Unique Options: Each question must have 4 answer options.\nAll options must be unique; avoid duplicates.\nThe correct answer must be one of the provided options, and case-sensitive where necessary.\n\n\nCorrect Answer & Feedback:\nCorrect Answer: Must be accurate and based on information from the document.\nFeedback: Should explain why the correct answer is accurate but should not reference specific sections of the document or ask where events occurred.\n\nQuiz Name:\nCreative Title: Generate a creative name for the quiz  from the TEXT passed  to you\n\nInput Format:\nPDF\nDifficulty Level\n\n\nOutput Format:\nJSON Structure: Return the result in the following JSON format:\n\n{\n    "name": "Creative Quiz Title",  \n "time" : 1800 \n    "questions": [\n        {\n            "question": "Sample question text?",\n            "options": ["Option1", "Option2", "Option3", "Option4"],\n            "correctAnswer": "CorrectOption",\n            "feedBack": "Explanation of why CorrectOption is the right answer, referencing information from the document."\n        },\n        {\n            "question": "Another question?",\n            "options": ["OptionA", "OptionB", "OptionC", "OptionD"],\n            "correctAnswer": "OptionC",\n            "feedBack": "Explanation of why OptionC is correct."\n        }\n    ]\n}\n\nExample JSON Output:\n{\n    "name": "COS121 Programming Concepts Quiz",\n  "time": 1800  "questions": [\n        {\n            "correctAnswer": "To solve complex problems",\n            "feedBack": "Algorithms are designed to provide step-by-step solutions to complex problems, breaking them down into manageable steps.",\n            "options": [\n                "To write efficient code",\n                "To solve complex problems",\n                "To design a user interface",\n                "To optimize memory usage"\n            ],\n            "question": "What is the primary goal of algorithm design in programming?"\n        },\n        {\n            "correctAnswer": "To design algorithms",\n            "feedBack": "Flowcharts visually represent the steps and logic of an algorithm, aiding in its design and understanding.",\n            "options": [\n                "To write code",\n                "To design algorithms",\n                "To debug programs",\n                "To test software"\n            ],\n            "question": "What is a flowchart used for in programming?"\n        },\n        {\n            "correctAnswer": "To identify reserved words",\n            "feedBack": "Keywords are reserved words with special meanings; they define the program\'s structure and syntax and cannot be used as variable names.",\n            "options": [\n                "To declare variables",\n                "To define functions",\n                "To control program flow",\n                "To identify reserved words"\n            ],\n            "question": "What is the purpose of keywords in programming?"\n        },\n        {\n            "correctAnswer": "Assignment assigns a value, while equality checks for equality",\n            "feedBack": "The assignment operator (=) assigns a value, while the equality operator (==) compares values.",\n            "options": [\n                "Assignment checks for equality, while equality assigns a value",\n                "Assignment and equality are the same",\n                "Assignment is used for arithmetic operations",\n                "Assignment assigns a value, while equality checks for equality"\n            ],\n            "question": "What is the difference between assignment and equality operators?"\n        },\n        {\n            "correctAnswer": "Loop",\n            "feedBack": "Loops are control structures that repeatedly execute a block of code until a condition is met.",\n            "options": [\n                "Conditional statement",\n                "Loop",\n                "Function",\n                "Array"\n            ],\n            "question": "What type of control structure is used to execute a block of code repeatedly?"\n        },\n        {\n            "correctAnswer": "To store a collection of values",\n            "feedBack": "Arrays efficiently store and manage multiple values of the same data type.",\n            "options": [\n                "To store a single value",\n                "To store a collection of values",\n                "To perform arithmetic operations",\n                "To control program flow"\n            ],\n            "question": "What is the purpose of an array in programming?"\n        },\n        {\n            "correctAnswer": "A block of code that performs a specific task",\n            "feedBack": "Functions encapsulate a specific task, improving code organization and reusability.",\n            "options": [\n                "A variable that stores a value",\n                "A control structure that executes code repeatedly",\n                "A data structure that stores a collection of values",\n                "A block of code that performs a specific task"\n            ],\n            "question": "What is a function in programming?"\n        },\n        {\n            "correctAnswer": "To promote code reusability",\n            "feedBack": "Functions promote code reusability by allowing the same code block to be used multiple times, reducing redundancy.",\n            "options": [\n                "To reduce code readability",\n                "To increase code complexity",\n                "To promote code reusability",\n                "To decrease code efficiency"\n            ],\n            "question": "What is the benefit of using functions in programming?"\n        },\n        {\n            "correctAnswer": "Local variables are accessible only within a function, while global variables are accessible throughout the program",\n            "feedBack": "Local variables have limited scope within a function, while global variables are accessible from anywhere in the program.",\n            "options": [\n                "Local variables are accessible globally, while global variables are accessible locally",\n                "Local variables are accessible only within a function, while global variables are accessible throughout the program",\n                "Local variables are used for arithmetic operations, while global variables are used for storing strings",\n                "Local variables are used for storing arrays, while global variables are used for storing single values"\n            ],\n            "question": "What is the difference between a local variable and a global variable?"\n        },\n        {\n            "correctAnswer": "To explain code functionality",\n            "feedBack": "Comments enhance code readability and understanding by explaining the purpose and functionality of code sections.",\n            "options": [\n                "To execute code",\n                "To declare variables",\n                "To control program flow",\n                "To explain code functionality"\n            ],\n            "question": "What is the purpose of comments in programming?"\n        },\n        {\n            "correctAnswer": "Input, Processing, Output",\n            "feedBack": "An algorithm takes input, processes it, and produces output; these are fundamental steps in its operation.",\n            "options": [\n                "Input, Processing, Output",\n                "Finiteness, Definiteness, Effectiveness",\n                "Start, Process, Stop",\n                "Decision, Loop, End"\n            ],\n            "question": "What are the three fundamental components of an algorithm?"\n        },\n        {\n            "correctAnswer": "Oval",\n            "feedBack": "The oval shape is used to denote the start and end points of a flowchart.",\n            "options": [\n                "Rectangle",\n                "Diamond",\n                "Parallelogram",\n                "Oval"\n            ],\n            "question": "Which flowchart symbol represents the start or end of a process?"\n        },\n        {\n            "correctAnswer": "Diamond",\n            "feedBack": "The diamond shape is used to represent decision points in a flowchart, where different paths are possible based on a condition.",\n            "options": [\n                "Rectangle",\n                "Oval",\n                "Parallelogram",\n                "Diamond"\n            ],\n            "question": "Which flowchart symbol represents a decision point?"\n        },\n        {\n            "correctAnswer": "Parallelogram",\n            "feedBack": "A parallelogram denotes input or output operations within a flowchart.",\n            "options": [\n                "Rectangle",\n                "Diamond",\n                "Parallelogram",\n                "Oval"\n            ],\n            "question": "Which flowchart symbol represents input or output?"\n        },\n        {\n            "correctAnswer": "int",\n            "feedBack": "The keyword \\"int\\" is used to declare integer variables in many programming languages.",\n            "options": [\n                "char",\n                "double",\n                "float",\n                "int"\n            ],\n            "question": "Which keyword is commonly used to declare integer variables?"\n        },\n        {\n            "correctAnswer": "double",\n            "feedBack": "The keyword \\"double\\" is used to declare variables that can store floating-point numbers with greater precision.",\n            "options": [\n                "int",\n                "char",\n                "float",\n                "double"\n            ],\n            "question": "Which keyword is used to declare a variable that can store floating-point numbers?"\n        },\n        {\n            "correctAnswer": "char",\n            "feedBack": "The keyword \\"char\\" is used to declare variables that can store single characters.",\n            "options": [\n                "int",\n                "double",\n                "float",\n                "char"\n            ],\n            "question": "Which keyword is used to declare a variable that can store a single character?"\n        },\n        {\n            "correctAnswer": "Variable names must start with a letter or underscore.",\n            "feedBack": "Variable names must adhere to specific rules to ensure clarity and avoid conflicts; they must start with a letter or underscore and cannot be keywords.",\n            "options": [\n                "Variable names can contain spaces.",\n                "Variable names can start with a number.",\n                "Variable names can be keywords.",\n                "Variable names must start with a letter or underscore"\n            ],\n            "question": "Which of the following is a rule for naming variables?"\n        },\n        {\n            "correctAnswer": "if-else statement",\n            "feedBack": "The if-else statement allows for conditional execution of code blocks based on a condition\'s truth value.",\n            "options": [\n                "for loop",\n                "while loop",\n                "switch statement",\n                "if-else statement"\n            ],\n            "question": "Which control structure allows for conditional execution of code blocks?"\n        },\n        {\n            "correctAnswer": "For loop",\n            "feedBack": "The for loop is designed for iterating a specific number of times, making it suitable for repetitive tasks with a known number of iterations.",\n            "options": [\n                "while loop",\n                "do-while loop",\n                "if-else statement",\n                "For loop"\n            ],\n            "question": "Which loop is best suited for iterating a specific number of times?"\n        }\n    ]\n}\nAdditional Notes:\n\nEnsure Correctness: The correct answer must be accurate and based strictly on the provided documents.\nCase Sensitivity: Pay close attention to the casing of the correct answers to avoid case-related errors.\nFeedback Quality: Ensure feedback provides meaningful, non-redundant explanations. Avoid overly simple phrasing and offer valuable context about the correct answer.\nUser Modifications: If users modify the prompt, maintain the existing JSON structure. Do not alter the schema.\nDocument Integrity: Input documents or text  should be clean, properly formatted to avoid issues with data processing.\nJSON Validation: Double-check that the JSON output is valid, adheres to the correct structure, and ensures all data types (e.g., strings, arrays) are correctly formatted before submission.\nOptions must be a maximum of 8 words for each option\nnumber of questions generated must be 20\nOptions when difficult level is set tio HARD must be a maximum  of 10 words for each option',
)


# Reuse chat session
chat_session = model.start_chat(history=[])


async def quiz_engine(extracted_text=None, difficult_level=None):

    # pass in the extrated text from the pdf to "extracted_text"
    extracted_text = extracted_text or "Introduction to computer Programming"
    # pass in the difficult level selected by the user [HARD, MEDIUM, EASY]
    difficult_level = difficult_level or "MEDIUM"

    # takes difficult level in a new line for the model to understand
    input_data = f"{extracted_text}\n{difficult_level}"

    loop = asyncio.get_event_loop()
    try:
        response = await asyncio.wait_for(
            loop.run_in_executor(None, chat_session.send_message, input_data),
            timeout=15,
        )
        response = json.loads(response.text)
        res = response if "questions" in response else None
        return res
    except Exception:
        return None
