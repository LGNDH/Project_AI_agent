def main():
    import os
    from dotenv import load_dotenv
    from functions.generate_content import generate_content
    from functions.call_function import call_function
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
    
    for _ in range(20):
        #call generate content function
        response = generate_content(client, messages)

        #making sure that agent have previous responses avaiable
        for item in response.candidates:
            messages.append(item.content)

        #output to console
        if args.verbose == True:
            print("User prompt: ", args.Agent_request)
            print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
            print("Response tokens: ", response.usage_metadata.candidates_token_count)

       
        functions_result_list = []
        if response.function_calls != None:
            for call in response.function_calls:
                function_call_result = call_function(call, verbose=args.verbose)
                if function_call_result.parts == []:
                    raise Exception("Error: function_call_result.parts is empty")
                if function_call_result.parts[0].function_response == None:
                    raise Exception("Error: function_call_result.parts[0].function_response is None")
                if function_call_result.parts[0].function_response.response == None:
                    raise Exception("Error: function_call_result.parts[0].function_response.response is None")
                else:
                    functions_result_list.append(function_call_result.parts[0])
                if args.verbose == True:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                messages.append(types.Content(role="user", parts=functions_result_list))
        
        else:   
            print(response.text)
            break
        if _ == 20:
            print("Error: AI agent went through maximum number of repeated calls")
            sys.exit(1)

if __name__ == "__main__":
    main()
