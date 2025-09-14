from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyBNOYj40SLcfprE5v2ABDhjb36_nBYLNU0"
API_URL = "https://api.openai.com/v1/images/generations"  # thay bằng endpoint Gemini thật nếu khác

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt", "")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"prompt": prompt, "size": "512x512"}

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        if "data" in result and len(result["data"]) > 0:
            image_b64 = result["data"][0]["b64_json"]
            return jsonify({"image": image_b64})
        else:
            return jsonify({"error": "Không nhận được ảnh từ API."})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
