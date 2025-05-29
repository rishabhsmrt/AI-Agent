import requests, sys, os
import json
import argparse

# To only run this function python3 connect_model.py model_respnse "Hello"

def model_response(prompt, model="mistral:latest", api_url="http://localhost:11434/api/generate",):
    """
    Sends a POST request to the local OLLAMA API to generate response.

    Parameters:
        prompt (str): The input prompt for the model.
        model (str): The name of the model to use. Default is "mistral".
        api_url (str): The URL of the local Mistral API. Default is "http://localhost:11434/api/generate".

    Returns:
        str: The generated text response from the model.
    """



    payload = {
        "model": model,
        "prompt": prompt
    }

    try:
        response = requests.post(api_url, data=json.dumps(payload), headers={"Content-Type": "application/json"}, stream=True)
        response.raise_for_status()  # Raise an error for HTTP error responses
        return format_response(response.iter_lines())

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    

def format_response(lines):
    """
    Formats and appends streamed response lines into a coherent text.

    Parameters:
        lines (iterable): Streamed lines from the response.

    Returns:
        str: The concatenated text from the streamed response.
    """

    full_response = ""
    
    for line in lines:
        try:
            # Parse each line as JSON
            data = json.loads(line)
            full_response += data.get("response", "")
        except json.JSONDecodeError:
            continue  # Ignore lines that are not valid JSON
    
    return full_response

# python3 connect_model.py model_response "Hi, how are you?"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Display the input string provided via the command line.")
    parser.add_argument("input_string", type=str, help="The string to display.")
    
    prompt = parser.parse_args().input_string
    response = model_response(prompt)
    print(response)


