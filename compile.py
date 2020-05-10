import speech_recognition as sr 
import pyttsx3  
from predict import init, predict
import time
from show import show_init, paint, pred_show

screen = show_init()

posx = 0
posy = 0
model, char_to_int, int_to_char, n_vocab = init()
print(char_to_int)

r = sr.Recognizer()
audio3=[]
text = ''
start = True
while(start):

    try:
        start = time.time()
        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.3)

            speaking = True

            while(speaking):

                audio2 = r.listen(source2)

                Mytext = r.recognize_google(audio2)
                Mytext = Mytext.lower()
                posx, posy = paint(screen, Mytext, posx, posy)
                text  += '.'+ Mytext
                print(len(text))
                if(len(text) > 100):
                    text = text[(len(text)-100):len(text)]
                    print(text)
                    Predicted_text = predict(text, char_to_int, int_to_char, model, n_vocab)
                    print(Predicted_text)
                    pred_show(screen, Predicted_text, posx, posy)
                
                if(text[len(text)-4:] == 'quit'):
                    speaking = False
                    start = False




            

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        
    except sr.UnknownValueError: 
        print("unknown error occured") 