from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    """Perform sentiment analysis using TextBlob."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return {"sentiment": "Positive", "score": polarity}
    elif polarity < 0:
        return {"sentiment": "Negative", "score": polarity}
    else:
        return {"sentiment": "Neutral", "score": polarity}

@app.route("/sentiment", methods=["POST"])
def sentiment():
    """API endpoint for sentiment analysis."""
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Text input required"}), 400

    result = analyze_sentiment(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
