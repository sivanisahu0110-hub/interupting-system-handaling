import webrtcvad
from config import VAD_AGRESSIVENESS

class VoiceDetector:
    def __init__(self):
        self.vad = webrtcvad.Vad(VAD_AGRESSIVENESS)

    def detect_speech(self, audio_frame, sample_rate):
        return self.vad.is_speech(audio_frame, sample_rate)