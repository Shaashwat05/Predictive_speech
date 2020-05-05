import speech_recognition as sr 
import pyttsx3  
from pydub import AudioSegment
from lookup import lookup,init,get_sites
from clean import cleanup, array



web = cleanup()
key_words = array(web)

kw = init(key_words)

r = sr.Recognizer()

while(1):

    try:

        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=2)

            audio2 = r.listen(source2)

            Mytext = r.recognize_google(audio2)
            Mytext = Mytext.lower()
            sites = lookup(kw, Mytext)
            site = get_sites(sites,key_words, web)
            print(site)

            

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        
    except sr.UnknownValueError: 
        print("unknown error occured") 