from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests


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
    auth = request.headers.get("Authorization")
    headers = {
        "Content-Type": "application/json",
        "Authorization": auth,
    }

    response = requests.post(
        "https://api.anthropic.com/v1/chat/completions",
        headers=headers,
        json=json_data,
    )
    if response.status_code != 200:
        return response.text, response.status_code
    result = response.json()
    return result


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5001,
    )
