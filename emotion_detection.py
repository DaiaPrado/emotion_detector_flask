import requests

def emotion_detector(text_to_analyse):
    
    #url to which the text will be sent
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    #Model to use to analyze text
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    #dictionary with text to analyze. 
    myobj= { "raw_document": { "text": text_to_analyse } }

    #Send a post request to the API. 
    response = requests.post(url, json=myobj, headers=header)

    return response.text #Return the response text from the API