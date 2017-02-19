import _Voice
import _Youtube


#Assign:
YoutubeSearch = _Youtube.YoutubeSearch
Speak = _Voice.Speak


while True:
    Audio = _Voice.Listen()
    Recognized = _Voice.Recognize(Audio)
    if Recognized != None:
        print('[I heard]: ' + str(Recognized))
    else:
        pass
