import speech_recognition as sr 
import pyttsx3  
from predict import init, predict
import time
from show import show_init, paint, pred_show

#pygame initialization
screen = show_init()

posx = 0
posy = 0

#model initialization
model, char_to_int, int_to_char, n_vocab = init()


#speech recognizer initialization
r = sr.Recognizer()
m = sr.Microphone()

audio3=[]
text = ''
start = True
time.sleep(15)
while(start):

    try:
        with m as source:

            r.adjust_for_ambient_noise(source)
            
            
            print("start speaking")
            audio = r.listen(source)
            Mytext = r.recognize_google(audio)
            Mytext = Mytext.lower()
            Mytext += '. '  
            screen, posx, posy = paint(screen, Mytext, posx, posy)
            text += Mytext
            if(len(text) > 100):
                text = text[(len(text)-100):len(text)]
                Predicted_text = predict(text, char_to_int, int_to_char, model, n_vocab)
                print(Predicted_text)
                screen = pred_show(screen, Predicted_text, posx, posy)
            
            if(text[len(text)-4:] == 'quit'):
                #speaking = False
                start = False




            

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        
    except sr.UnknownValueError: 
        print("unknown error occured") 