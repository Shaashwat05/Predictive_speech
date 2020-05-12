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
client, char_to_int, int_to_char, n_vocab, scoring_endpoint = init()


#speech recognizer initialization
r = sr.Recognizer()
m = sr.Microphone()

audio3=[]
text = ''
start = True
while(start):

    try:
        start = time.time()
        with m as source:

            r.adjust_for_ambient_noise(source)

            
            print("start speaking")
            audio2 = r.listen(source)
            print("listen" , (time.time() - start))
            Mytext = r.recognize_google(audio2)
            print("text", (time.time()-start))
            Mytext = Mytext.lower()
            Mytext += '. '  
            screen, posx, posy = paint(screen, Mytext, posx, posy)
            print("pygame", (time.time()-start))
            if(len(text) > 100):
                text = text[(len(text)-100):len(text)]
                Predicted_text = predict(text, char_to_int, int_to_char, client, n_vocab, scoring_endpoint)
                print(Predicted_text)
                screen = pred_show(screen, Predicted_text, posx, posy)
            
            if(text[len(text)-4:] == 'quit'):
                #speaking = False
                start = False




            

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        
    except sr.UnknownValueError: 
        print("unknown error occured") 