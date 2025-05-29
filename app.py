from flask import Flask, render_template, request
from datetime import datetime
from modules.LLM import generate_response


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        prompt = request.args.get('prompt', '')
        response = generate_response(prompt, "realestate_granite3.1-moe:1b")
    return response


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
    