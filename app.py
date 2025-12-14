import os

from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

classifier = pipeline(
    "text-classification",
    model="cybersectony/phishing-email-detection-distilbert_v2.1"
)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/checker")
def checker():
    return render_template("checker.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("email")
    result = classifier(text)
    return jsonify(result)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)