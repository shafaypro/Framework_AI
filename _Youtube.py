import speech_recognition as sr
import stopit #timeout module

r = sr.Recognizer()
m = sr.Microphone()
def Listen():
    with m as source:
        x = r.adjust_for_ambient_noise(source, duration = 1)
        print('[Listener]: Listening')
        with stopit.ThreadingTimeout(5) as to_ctx_mgr:
            assert to_ctx_mgr.state == to_ctx_mgr.EXECUTING
            audio = r.listen(source)
        if to_ctx_mgr.state == to_ctx_mgr.EXECUTED:
            return audio
        else:
            print('[Info]: Listener timed out.')
            return None
            pass
def Recognize(Audio):
    if Audio != None:
        try:
            return r.recognize_google(Audio)
        except:
            print('[Info]: Failed to recognize.')
    else:
        print('[Info]: Timeout detected. Restarting...')
        pass
