import sys, os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.LLM import generate_response

def save_benchmark_prompts(folder_name, file_name, prompt, response, model):

    current_dir = os.getcwd()
    
    # Determine the parent directory (one level up)
    parent_dir = os.path.dirname(current_dir)
    
    # Create the full path for the new folder in the parent directory
    folder_path = os.path.join(parent_dir, f".logs/{model}")
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Define the full path for the file
    file_path = os.path.join(folder_path, file_name)
    
    # Write "hello world" to the file
    with open(file_path, 'w') as file:
        file.write(f"Prompt : {prompt} \nResponse : {response} \n")
    
if __name__ == "__main__":

    models = ["finetune_granite3.1-moe:1b"]

    benchmark_prompts = open("../data/benchmark_prompts.txt", "r")
    for prompt in benchmark_prompts:
        for model in models:
            response = generate_response(prompt, model)
            save_benchmark_prompts(model, datetime.now().strftime("%Y%m%d_%H%M%S"), prompt, response, model)






