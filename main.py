def main():
    import os
    from dotenv import load_dotenv
    import argparse
    from google import genai
    from google.genai import types


    # load api key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None:
        raise RuntimeError("No api_key found")


    
    #create a gemini client
    client = genai.Client(api_key=api_key)

    #prompt from user, using argparse
    parser = argparse.ArgumentParser(description="AI_agent")
    parser.add_argument("Agent_request", type=str, help="Hello, please write your request.")
    args = parser.parse_args()


    #Prompt to client
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=args.Agent_request
    )
    if response.usage_metadata == None:
        raise RuntimeError("Failed api request")
    
    #printing answer and to terminal
    print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
    print("Response tokens: ", response.usage_metadata.candidates_token_count)
    print(response.text)
    
    #Saving User's imputs
    messages = 
    

if __name__ == "__main__":
    main()
