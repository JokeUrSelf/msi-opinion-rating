from flask import jsonify, request
from utils.routing import route
from model.model import sentiment_analyzer


@route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    sentiment_analyzer.polish(text)
    result = sentiment_analyzer.polish(text)
    return jsonify(result[0])