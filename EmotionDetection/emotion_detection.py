import requests
import json

def emotion_detector(text_to_analyse):
    
    #url to which the text will be sent
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    #Model to use to analyze text
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    #dictionary with text to analyze. 
    myobj= { "raw_document": { "text": text_to_analyse } }

    #Send a post request to the API. 
    response = requests.post(url, json=myobj, headers=header)

    #Formating response to json
    json_response = json.loads(response.text)
    print("STATUS: ", response.status_code)
    print("TEXT: ", text_to_analyse)

    if response.status_code == 200:
        #scores of each emotion
        anger_score = json_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = json_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = json_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = json_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = json_response["emotionPredictions"][0]["emotion"]["sadness"]

        #dictionary of emotions from the json_response output. 
        emotions = json_response["emotionPredictions"][0]["emotion"]
        dominant_emotion =  max(emotions, key=emotions.get)

    if response.status_code == 400:
        print("SI ENTRE")
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return {'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }