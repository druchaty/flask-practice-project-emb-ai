''' Docstring
'''
import json
import requests

def sentiment_analyzer(text_to_analyse):
    ''' Docstring
    '''
    # URL of the sentiment analysis service
    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = { "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock" }

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json = myobj, headers = header, timeout=2)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    label = None
    score = None

    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

    # Returning a dictionary containing sentiment analysis results
    return { "label": label, "score": score }



    # Importing function in the Python console:
    # from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
    # Install pylint:
    # python -m pip install pylint
    # Run:
    # pylint <file_name>
