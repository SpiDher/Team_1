# Quiz generator model 
-Generated quiz from text 

## Schema, inputs type and format of quiz
- An asychrinous function that takes 2 inputs (Extracted text from pdf and the diffuculty leve)
- Then generates 20 quiz using from the text passed to it as input 
produces output in json format 
example output
{
    "name": "Creative Quiz Title",
    "questions": [
        {
            "question": "Sample question text?",
            "options": ["Option1", "Option2", "Option3", "Option4"],
            "correctAnswer": "CorrectOption",
            "feedBack": "Explanation of why CorrectOption is the right answer, referencing information from the document."
        },
        {
            "question": "Another question?",
            "options": ["OptionA", "OptionB", "OptionC", "OptionD"],
            "correctAnswer": "OptionC",
            "feedBack": "Explanation of why OptionC is correct."
        }
    ]
}

-used data schema to help prevent the output from going out of structure as it might cause the quiz to fail
schema Used:
"response_schema": content.Schema(
    type = content.Type.OBJECT,
    enum = [],
    required = ["name", "questions"],
    properties = {
      "name": content.Schema(
        type = content.Type.STRING,
      ),
      "questions": content.Schema(
        type = content.Type.ARRAY,
        items = content.Schema(
          type = content.Type.OBJECT,
          enum = [],
          required = ["question", "options", "correctAnswer", "feedBack"],
          properties = {
            "question": content.Schema(
              type = content.Type.STRING,
            ),
            "options": content.Schema(
              type = content.Type.ARRAY,
              items = content.Schema(
                type = content.Type.STRING,
              ),
            ),
            "correctAnswer": content.Schema(
              type = content.Type.STRING,
            ),
            "feedBack": content.Schema(
              type = content.Type.STRING,
            ),
          },
        ),
      ),
    },
  )

  suppressed absl loggin so the output would just be the quiz 
