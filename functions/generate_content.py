#Function to prompt user
from prompts import system_prompt
from google.genai import types
from function_declaration_LLM import available_functions


def generate_content(client, messages):
    #Prompt to client
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )
    if response.usage_metadata == None:
        raise RuntimeError("Failed api request")
    
    return response

    