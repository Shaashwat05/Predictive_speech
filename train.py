import sys
import numpy as np 
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
import pickle

filename = "wonderland.txt"
raw_text = open(filename, 'r', encoding='utf-8').read()
raw_text = raw_text.lower()

chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i,c in enumerate(chars))
int_to_char = dict((i, c) for i,c in enumerate(chars))

ci  =  open("variables/c2i.pkl", "wb")
pickle.dump(char_to_int, ci)
ci.close()

ic = open("variables/i2c.pkl", "wb")
pickle.dump(int_to_char, ic)
ic.close()

n_chars = len(raw_text)
n_vocab = len(chars)

voc = open("variables/n_vocab.pkl", "wb")
pickle.dump(n_vocab, voc)
voc.close()


seq_length = 100
dataX = []
dataY = []

for i in range(0, n_chars - seq_length, 1):
    seq_in = raw_text[i:i + seq_length]
    seq_out = raw_text[i+seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])

n_patterns = len(dataX)

print("total characters :", n_chars)
print("\n")
print("total vocab :", n_vocab)
print("\n")
print("total patterns :", n_patterns)
print("\n")
print("DataX Sample :", dataX[1])
print("\n")
print("DataY Sample :", dataY[1])

X = np.reshape(dataX, (n_patterns, seq_length, 1))
X =X/ float(n_vocab)

y = np_utils.to_categorical(dataY)



model = Sequential()
model.add(LSTM(256, input_shape = (X.shape[1], X.shape[2]), return_sequences = True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam')

filepath = "weights/weights-improvement-{epoch:02d}-{loss:.4f}-biggeer.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose = 1, save_best_only=True, mode = 'min')
callbacks_list = [checkpoint]

#model = load_model("weights/weights-improvement-02-2.2221-biggee.hdf5")

model.fit(X, y, epochs = 50, batch_size=64, callbacks=callbacks_list)
model.save("model.hdf5", model)


