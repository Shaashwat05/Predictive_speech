#import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np 
import pickle
from watson_machine_learning_client import WatsonMachineLearningAPIClient


def init(): # initializing IBM credentials and model
    model = load_model("weights/model.hdf5")

    
    wml_credentials={
    "url": "xxxxxxxxxxxxxxxxxx",
    "apikey": "xxxxxxxxxxxxxxxxxxxxxxx",
    "username": "xxxxxxxxxxxxxxxxxxxx",
    "password": "xxxxxxxxxxxxxxxxxxxxxxx",
    "instance_id": "xxxxxxxxxxxxxxxxxxxxxx"
    }
    

    # IBM deployment initialization
    client = WatsonMachineLearningAPIClient(wml_credentials)

    #deployment = pickle.load(open("variables/deployment.pkl", "rb"))
    char_to_int = pickle.load(open("variables/c2i.pkl", "rb"))
    int_to_char = pickle.load(open("variables/i2c.pkl", "rb"))
    n_vocab = pickle.load(open("variables/n_vocab.pkl", "rb"))

    #scoring_endpoint = client.deployments.get_scoring_url(deployment)
    scoring_endpoint = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    return client, char_to_int, int_to_char, n_vocab, scoring_endpoint



def predict(text_in, char_to_int, int_to_char, client, n_vocab, scoring_endpoint):  # prediction of speech
    text1=[]
    out = ''

    print(text_in)
    for i in text_in:
        text1.append(char_to_int[i]) 

    for i in range(100):
        text = np.reshape(text1, (1, len(text1), 1))
        text = text /float(n_vocab)

        scoring_payload = {'values': text.tolist()}
        predict = client.deployments.score(scoring_endpoint, scoring_payload)
        #predict = model.predict(text, verbose = 0)

        index = np.argmax(predict)
        result = int_to_char[index]
        #seq_in = [int_to_char[value] for value in text1]
        out +=result
        text1.append(index)
        text1 = text1[1:len(text1)]

    return out

'''
client, char_to_int, int_to_char, n_vocab, scoring_endpoint = init()

text_in = "so she was considering in her own mind (as well as she could, for the hot day made her feel very sle"

text = predict(text_in, char_to_int, int_to_char, client, n_vocab, scoring_endpoint)
print(text)
'''