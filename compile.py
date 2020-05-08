import speech_recognition as sr 
import pyttsx3  
from pydub import AudioSegment
from predict import init, predict
import time

model, int_to_char, char_to_int, n_vocab = init()

r = sr.Recognizer()
audio3=[]
text = ''
while(1):

    try:
        start = time.time()
        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.5)

            audio2 = r.listen(source2)
            audio3.append(audio2)

            Mytext = r.recognize_google(audio2)
            Mytext = Mytext.lower()
            text  += ' '+ Mytext
            print(len(text))
            if(len(text) > 100):
                print(text)
                text = text[(len(text)-100):len(text)]
                Predicted_text = predict(text, char_to_int, int_to_char, model, n_vocab)
                print("\n")
                print(Predicted_text)




            

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        
    except sr.UnknownValueError: 
        print("unknown error occured") 