import requests
import json

def emotion_detector(text_to_analyze):
    # Url of the Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Custom header specifying the model ID for the Emotion Predict service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Constructing the request payload in the expected format
    json_input = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the Emotion Predict API
    response = requests.post(url, json=json_input, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    emotions_scores = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions_scores, key=emotions_scores.get)

    # Returning a dictionary with the Emotion Predict results
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
