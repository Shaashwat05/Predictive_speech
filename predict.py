import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np 
import pickle
from watson_machine_learning_client import WatsonMachineLearningAPIClient


def init():

    wml_credentials={
    "url": "xxxxxxxxxxxxxxxxxx",
    "apikey": "xxxxxxxxxxxxxxxxxxxxxxx",
    "username": "xxxxxxxxxxxxxxxxxxxx",
    "password": "xxxxxxxxxxxxxxxxxxxxxxx",
    "instance_id": "xxxxxxxxxxxxxxxxxxxxxx"
    }

    # IBM deployment initialization
    client = WatsonMachineLearningAPIClient(wml_credentials)

    deployment = pickle.load("variables/deployment.pkl", "rb")
    char_to_int = pickle.load(open("variables/c2i.pkl", "rb"))
    int_to_char = pickle.load(open("variables/i2c.pkl", "rb"))
    n_vocab = pickle.load(open("variables/n_vocab.pkl", "rb"))

    scoring_endpoint = client.deployments.get_scoring_url(deployment)

    return client, char_to_int, int_to_char, n_vocab, scoring_endpoint



def predict(text_in, char_to_int, int_to_char, client, n_vocab, scoring_endpoint):
    text1=[]
    out = ''
    print(text_in)
    for i in text_in:
        text1.append(char_to_int[i]) 
    for i in range(100):
        text = np.reshape(text1, (1, len(text1), 1))
        text = text /float(n_vocab)
        scoring_payload = {'values': text}
        predict = client.deployments.score(scoring_endpoint, scoring_payload)
        index = np.argmax(predict)
        result = int_to_char[index]
        #seq_in = [int_to_char[value] for value in text1]
        out +=result
        text1.append(index)
        text1 = text1[1:len(text1)]

    return out

'''
model, char_to_int, int_to_char, n_vocab = init()

text_in = "hashwat.i study in assam valley school.i want to be a engineer one day.i want to study in iit mumbai"

text = predict(text_in, char_to_int, int_to_char, model, n_vocab)
print(text)'''
import keras

print(keras.__version__)