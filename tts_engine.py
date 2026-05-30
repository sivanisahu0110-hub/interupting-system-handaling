import pyttsx3
import threading

class TTSEngine:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.speaking = False

    def speak(self, text):
        self.speaking = True

        def run():
            self.engine.say(text)
            self.engine.runAndWait()
            self.speaking = False

        threading.Thread(target=run).start()

    def stop(self):
        self.engine.stop()
        self.speaking = False