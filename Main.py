import _VoiceRec


while True:
    Audio = _VoiceRec.Listen()
    Recognized = _VoiceRec.Recognize(Audio)
    if Recognized != None:
        print('[I heard]: ' + str(Recognized))
    else:
        pass
