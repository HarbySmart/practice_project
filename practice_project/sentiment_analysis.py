import requests
import json


def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)
    #returning the output in form of a dictionary instead of text using the json library
    formatted_response = json.loads(response.text)
    
    #extract the needed output from the nested dictionary in form of a dictionary with keys label and score
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    return {"label": label, "score": score}