'''This is the main document'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detector")

@app.route("/emotionDetector")
def emotions_detection():
    '''This function sends the text to the emotion detector function, 
    obtains and displays the result of the detected emotion'''

    #Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    #Pass the text to analyze to our emotion detector function
    response = emotion_detector(text_to_analyze)

    if response["anger"] is None:
        text_to_return = "Invalid text! Please try again."

    else:
        text_to_return = (
                            f"For the given statement, the system response is "
                            f"'anger': {response['anger']}, "
                            f"'disgust': {response['disgust']}, "
                            f"'fear': {response['fear']}, "
                            f"'joy': {response['joy']} and "
                            f"'sadness': {response['sadness']}. "
                            f"The dominant emotion is {response['dominant_emotion']}."
                        )

    return text_to_return

@app.route("/")
def render_index_page():
    '''Renders the index.html'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
