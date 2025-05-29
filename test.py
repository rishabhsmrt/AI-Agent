import requests
import urllib.parse

def test_endpoint(prompt):
    base_url = "http://localhost:5000/"
    encoded_prompt = urllib.parse.quote(prompt)
    
    try:
        response = requests.get(f"{base_url}?prompt={encoded_prompt}")
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        print("Status Code:", response.status_code)
        print("Response:", response)
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

# Test cases
test_cases = [
    "Hello, how are you?",
]

for case in test_cases:
    print(f"\nTesting prompt: {case}")
    test_endpoint(case)