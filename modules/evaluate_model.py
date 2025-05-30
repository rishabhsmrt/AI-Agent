import requests, sys, os
import json
import argparse
from LLM import format_response
# To only run this function python3 connect_model.py model_respnse "Hello"

def evaluate_classifier_model(prompt, model="classifier_granite3.1-moe:1b", api_url="http://localhost:11434/api/generate",):
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
    

# python3 evaluate_model.py "user: Hi, how are you? assitant: I am fine thankyou. What are you looking for?"  

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Display the input string provided via the command line.")
    parser.add_argument("input_string", type=str, help="The string to display.")
    
    prompt = parser.parse_args().input_string
    response = evaluate_classifier_model(prompt)

    print(response)


