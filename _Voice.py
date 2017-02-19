import speech_recognition as sr
import stopit #timeout module
from gtts import gTTS
import pygame
from time import sleep as wait

r = sr.Recognizer()
m = sr.Microphone()

def Listen(): # Listener module activates mic, stores mp3
    with m as source:
        x = r.adjust_for_ambient_noise(source, duration = 1)
        print('[Listener]: Listening')
        with stopit.ThreadingTimeout(15) as to_ctx_mgr: #Set timeout values
            assert to_ctx_mgr.state == to_ctx_mgr.EXECUTING
            audio = r.listen(source)
        if to_ctx_mgr.state == to_ctx_mgr.EXECUTED:
            return audio
        else:
            print('[Info]: Listener timed out.') #if timeout happens, print fail.
            return None
            pass
        
def Recognize(Audio): #Sends mp3 to google to be translated
    if Audio != None:
        try:
            return r.recognize_google(Audio) #Sends mp3
        except:
            print('[Info]: Failed to recognize.') #Incase of failure, restart.
    else:
        print('[Info]: Timeout detected. Restarting...') #Same here as except
        pass

def Speak(Text):
    tts = gTTS(text=Text, lang='en')
    tts.save("Voice.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("Voice.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    wait(0.1)
