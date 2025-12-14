import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

HF_API_URL = "https://router.huggingface.co/hf-inference/models/cybersectony/phishing-email-detection-distilbert_v2.1"
HF_TOKEN = os.environ.get("HF_TOKEN")  # set in Render

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/checker")
def checker():
    return render_template("checker.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("email")

    response = requests.post(
        HF_API_URL,
        headers=headers,
        json={"inputs": text}
    )

    return jsonify(response.json())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
