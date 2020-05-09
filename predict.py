import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np 
import pickle


def init():
    model = load_model("weights/model.hdf5")

    char_to_int = pickle.load(open("variables/c2i.pkl", "rb"))
    int_to_char = pickle.load(open("variables/i2c.pkl", "rb"))
    n_vocab = pickle.load(open("variables/n_vocab.pkl", "rb"))

    return model, char_to_int, int_to_char, n_vocab



def predict(text_in, char_to_int, int_to_char, model, n_vocab):
    text1=[]
    out = ''
    print(text_in)
    for i in text_in:
        text1.append(char_to_int[i]) 
    for i in range(100):
        text = np.reshape(text1, (1, len(text1), 1))
        text = text /float(n_vocab)
        predict = model.predict(text, verbose = 0)
        index = np.argmax(predict)
        result = int_to_char[index]
        seq_in = [int_to_char[value] for value in text1]
        out +=result
        text1.append(index)
        text1 = text1[1:len(text1)]

    return out

'''
model, char_to_int, int_to_char, n_vocab = init()

text_in = "hashwat.i study in assam valley school.i want to be a engineer one day.i want to study in iit mumbai"

text = predict(text_in, char_to_int, int_to_char, model, n_vocab)
print(text)'''


