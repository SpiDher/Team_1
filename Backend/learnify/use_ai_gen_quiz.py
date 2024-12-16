from ai_gen_quiz_model import *

chat_session = model.start_chat(history=[])

# pass in the extrated text from the pdf to "extracted_text"
extracted_text = "Introduction to computer Science"
# pass in the difficult level selected by the user
difficult_level = "HARD"

# takes difficult level in a new line for the model to understand
input_data = f"{extracted_text}\n{difficult_level}"

response = chat_session.send_message(input_data)


print(response.text)
