import speech_recognition as sr 
import pyttsx3  
from pydub import AudioSegment


r = sr.Recognizer()

#audio_file = AudioSegment.from_wav('output.wav')



while(1):

    try:

        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=2)

            audio2 = r.listen(source2)

            Mytext = r.recognize_google(audio2)
            Mytext = Mytext.lower()

            print("Did you say" + Mytext)

    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
        
    except sr.UnknownValueError: 
        print("unknown error occured") 


'''with sr.AudioFile(audio_file) as source:
    audio = r.record(source) 
Mytext = r.recognize_google(audio)

print(Mytext)'''

    





