from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import requests

LLM_API_KEY = os.environ["LLM_API_KEY"]

app = Flask(__name__)

cors = CORS(app)  # allow CORS for all domains on all routes.
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
@cross_origin()
def home():
    return "Hello, World!"


@app.route("/about")
def about():
    return "About"


@app.route("/llm/v1/chat/completions", methods=["get", "post"])
def chat_completion():
    json_data = request.json
    if not json_data:
        return jsonify({"error": "Invalid request body"}), 400
    print("JSON data")
    print(json_data)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LLM_API_KEY}",
    }

    response = requests.post(
        "https://api.anthropic.com/v1/chat/completions",
        headers=headers,
        json=json_data,
    )
    response.raise_for_status()
    result = response.json()
    return result


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5001,
    )
