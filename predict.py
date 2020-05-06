from keras.models import load_model
import numpy as np 
import pickle


def init():
    model = load_model("weights/weights-improvement-02-2.2221-biggee.hdf5")

    char_to_int = pickle.load(open("variables/c2i.pkl", "rb"))
    int_to_char = pickle.load(open("variables/i2c.pkl", "rb"))
    n_vocab = pickle.load(open("variables/n_vocab.pkl", "rb"))

    return model, char_to_int, int_to_char, n_vocab



def predict(text_in, char_to_int, int_to_char, n_vocab):
    text=[]
    text.append(char_to_int[i] for i in text_in) 
    for i in range(100):
        text = np.reshape(text, (1, len(text), 1))
        text = text /float(n_vocab)
        predict = model.predict(x, verbose = 0)
        index = np.argmax(predict)
        result = int_to_char[index]
        seq_in = [int_to_char[value] for value in text]
        text.append(index)
        text = text[1:len(text)]

    return text



