from .ai_gen_quiz_model import *

def quiz_engine(extracted_text=None,difficult_level=None):
    chat_session = model.start_chat(history=[])

    # pass in the extrated text from the pdf to "extracted_text"
    extracted_text = extracted_text or "Introduction to computer Science"
    # pass in the difficult level selected by the user [HARD, MEDIUM, EASY]
    difficult_level = difficult_level or "HARD"

    # takes difficult level in a new line for the model to understand
    input_data = f"{extracted_text}\n{difficult_level}"

    response = chat_session.send_message(input_data)


    return response.text

