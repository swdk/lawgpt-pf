from promptflow import tool
from promptflow.connections import CustomConnection
import google.generativeai as genai

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str, conn: CustomConnection) -> str:
 
    genai.configure(api_key=conn.secrets['GEMINI_API_KEY'])
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content(input1, generation_config={
        # "max_output_tokens": 2048, 
        # "temperature": 1 
         }, 
                                      safety_settings=[
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "HIGH",
        }, 
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "HIGH",
        },
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "HIGH",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "HIGH",
        }
    ])   
    # print(response.candidates)
    return response.text
