import speech_recognition as sr 
import pyttsx3  
from pydub import AudioSegment
from predict import init, predict

#model, int_to_char, char_to_int, n_vocab = init()

r = sr.Recognizer()

while(1):

    try:

        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)

            Mytext = r.recognize_google(audio2)
            Mytext = Mytext.lower()
            print(Mytext)


            

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        
    except sr.UnknownValueError: 
        print("unknown error occured") 