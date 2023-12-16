from promptflow import tool

import pathlib
import textwrap

import google.generativeai as genai
import os
# Used to securely store your API key
# from google.colab import userdata

# from IPython.display import display
# from IPython.display import Markdown


# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

from promptflow.connections import CustomConnection


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str, conn: CustomConnection) -> str:
 
    genai.configure(api_key=conn.secrets['GEMINI_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content(input1, safety_settings=[
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "HIGH",
        }
    ])   

    print(response.prompt_feedback)

    return 'hello :' + response.text
