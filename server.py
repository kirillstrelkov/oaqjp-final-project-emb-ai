"""
This module contains a simple Flask web application
for detecting emotions in text using an external service.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")


@app.route("/")
def index():
    """
    Renders the index.html template.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyzes text provided via a URL query parameter and returns
    the emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    response = emotion_detector(text_to_analyze)

    if "dominant_emotion" not in response:
        return "Error in processing text. Check the emotion detection service.", 500

    dominant_emotion = response.pop("dominant_emotion")

    if not dominant_emotion:
        return "Invalid text! Please try again!", 400  # Changed to 400 status

    emotion_parts = []
    for key, value in response.items():
        emotion_parts.append(f"'{key}': {value}")

    if len(emotion_parts) > 1:
        scores_string = ", ".join(emotion_parts[:-1]) + " and " + emotion_parts[-1]
    elif len(emotion_parts) == 1:
        scores_string = emotion_parts[0]
    else:
        scores_string = ""

    return (
        f"For the given statement, the system response is {scores_string}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
