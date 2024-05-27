''' This file contains the code for
    running the sentiment analysis
'''
import json
import requests

def sentiment_analyzer(text_to_analyse):
    ''' we use the BERT based Sentiment Analysis
        function of the Watson NLP Library.
        For accessing this funciton, the URL, the headers and
        the input json format is as follows
    '''
    url = ('https://sn-watson-sentiment-bert.labs.skills.network/'
       'v1/watson.runtime.nlp.v1/NlpService/SentimentPredict')
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header, timeout=60)
    #returning the output in form of a dictionary instead of text using the json library
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        #extract the needed output from the nested dictionary in form
        #of a dictionary with keys label and score
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    else:
        label = None
        score = None

    return {"label": label, "score": score}
