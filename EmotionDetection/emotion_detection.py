import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=input_json, headers=headers)
    # If the response status code is 200, extract the label and score from the response
    scores={}
    dominant_emotion={}
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        #console.log(formatted_response)
        emotion_response = formatted_response['emotionPredictions'][0]['emotion']
        anger = emotion_response['anger']
        disgust = emotion_response['disgust']
        fear = emotion_response['fear']
        joy = emotion_response['joy']
        sadness = emotion_response['sadness']
        scores = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy,'sadness': sadness}
        dominant_emotion = max(scores, key=scores.get)
        
    # For any other unexpected status codes, set label and score to None
    else:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominantemotion = None

    # Return the scores
    
    return scores | { 'dominant_emotion': dominant_emotion}