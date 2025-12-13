from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load phishing detection model locally (one-time download)
classifier = pipeline(
    "text-classification",
    model="cybersectony/phishing-email-detection-distilbert_v2.1"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form.get("email")

    if not email_text:
        return jsonify({"error": "No email text provided"})

    result = classifier(email_text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
