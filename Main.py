import _VoiceRec
import _Youtube


#Assign:
YoutubeSearch = _Youtube.YoutubeSearch

while True:
    Audio = _VoiceRec.Listen()
    Recognized = _VoiceRec.Recognize(Audio)
    if Recognized != None:
        print('[I heard]: ' + str(Recognized))
    else:
        pass
