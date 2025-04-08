"""
This file contains a Flask web application that detects emotions from text.
It exposes an endpoint (/emotionDetector) that accepts POST requests with 
a JSON payload containing the text. The text is analyzed for emotions, and 
a response with the detected emotions and the dominant emotion is returned.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def emotion_detect():
    """
    Endpoint for detecting emotions from a given text.
    
    This function processes the incoming JSON data containing a 'text' field, 
    uses the emotion detector to analyze the text, and returns a JSON response 
    with the detected emotions and the dominant emotion.

    If the input text is empty or invalid, an error message is returned.
    If the emotion detector fails, an internal error response is provided.

    Returns:
        jsonify: A JSON response with either the emotion analysis or an error message.
    """
    # Get the incoming JSON data
    data = request.get_json()
    # Check if 'text' is present in the request data
    if "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    # Call emotion_detector function with the input text
    result = emotion_detector(data["text"])

    # Check if the 'text' field is empty or just spaces
    if not data["text"].strip():
        return jsonify({"result": "Invalid text! Please try again!"}), 400

    # Check if the result from emotion_detector contains required fields
    if "emotions" not in result or "dominant_emotion" not in result:
        return jsonify({"error": "Invalid response from emotion_detector"}), 500

    # Extract emotions and create a dictionary of emotion scores
    emotions = {item['label']: item['score'] for item in result['emotions']}
    target_emotions = ["anger", "disgust", "fear", "joy", "sadness"]

    # Construct the response message with the emotion scores
    response_parts = []
    for emotion in target_emotions:
        score = emotions.get(emotion, 0)
        response_parts.append(f"'{emotion}': {round(score, 3)}")

    # Construct the final response text
    response_text = (
        "For the given statement, the system response is " +
        ", ".join(response_parts) +
        f". The dominant emotion is {result['dominant_emotion']}."
    )

    # Return the response as a JSON
    return jsonify({"result": response_text})

if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)
