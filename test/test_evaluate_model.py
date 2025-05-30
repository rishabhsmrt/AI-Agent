import sys, os
from datetime import datetime
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from modules.LLM import generate_response

from test_connect_model import save_benchmark_prompts    

if __name__ == "__main__":
    models = ["classifier_granite3.1-moe:1b"]

    with open("../data/classifier_benchmark_prompts.txt", "r") as benchmark_file:
        benchmark_prompts = benchmark_file.readlines()
    
    
    for prompt in benchmark_prompts:
        for model in models:
            response = generate_response(prompt, model)
            time.sleep(1)
            save_benchmark_prompts(model, datetime.now().strftime("%Y%m%d_%H%M%S"), prompt, response, model)






