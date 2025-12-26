from flask import Flask, jsonify, request

app = Flask(__name__)

def detector(score):
    return {"result": "AI" if score >= 50 else "Human"}

@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    return jsonify(detector(data.get("score")))