def main():
    import os
    from dotenv import load_dotenv
    from functions.generate_content import generate_content
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
    parser.add_argument("--verbose", action="store_true", help="Enable/Disable verbose output")
    args = parser.parse_args()


    #Saving User's imputs
    messages = [types.Content(role="user", parts=[types.Part(text=args.Agent_request)])]
    
    #call generate content function
    response = generate_content(client, messages)
    
    #printing answer to terminal and if verbose arg true aditional data
    if args.verbose == True:
        print("User prompt: ", args.Agent_request)
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ", response.usage_metadata.candidates_token_count)

    if response.function_calls != None:
        for call in response.function_calls:
            print(f"Calling function: {call.name}({call.args})")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
