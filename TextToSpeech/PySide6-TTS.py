from PySide6 import QtTextToSpeech, QtCore

class tts(QtTextToSpeech.QTextToSpeech):
    def __init__(self):
        super().__init__()

    def init_voice_twitch(self):
        voice = QtTextToSpeech.QVoice()
        return voice
    
    def set_voice_twitch(self,voice : QtTextToSpeech.QVoice,name,gender,age,locale,language):
        voice.name = name
        voice.gender = gender
        voice.age = age
        voice.locale = locale
        voice.language = language

    def set_volume(self, number : float):
        self.volume = number

    def set_pitch(self, number : float):
        self.pitch = number

    def set_rate(self, number : float):
        self.rate = number

    def get_locale(self):
        return self.locale()
    
    def add_queue(self, text : str):
        self.enqueue(text)


tts_twitch = tts()
locale = tts_twitch.get_locale()
voice = tts_twitch.init_voice_twitch()
tts_twitch.set_voice_twitch(voice,
                            "Classic",
                            QtTextToSpeech.QVoice.Gender.Male,
                            20,
                            locale,
                            QtCore.QLocale.Language.French)
tts_twitch.set_volume(1.0)
tts_twitch.set_pitch(1.0)
tts_twitch.set_rate(0.0)
tts_twitch.state = QtTextToSpeech.QTextToSpeech.State.Ready
tts_twitch.say("Bonjour euuuh s'est michel")

