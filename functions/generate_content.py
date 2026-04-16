#Function to prompt user
def generate_content(client, messages):
    #Prompt to client
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
    )
    if response.usage_metadata == None:
        raise RuntimeError("Failed api request")
    
    return response

    