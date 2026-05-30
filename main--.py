import sounddevice as sd
import numpy as np
import json
import time

from vad_detector import VoiceDetector
from tts_engine import TTSEngine
from config import SPEECH_THRESHOLD, COOLDOWN_SECONDS

RATE = 16000
FRAME_DURATION = 30
FRAME_SIZE = int(RATE * FRAME_DURATION / 1000)

vad = VoiceDetector()
tts = TTSEngine()

last_interrupt_time = 0

speech_count = 0

last_interrupt_time = 0
state = "speaking"

print("Starting system...")

tts.speak(
    "Hello, I am your assistant. You can interrupt me anytime."
)

while True:

    audio = sd.rec(
        FRAME_SIZE,
        samplerate=RATE,
        channels=1,
        dtype='int16'
    )

    sd.wait()
    

    audio_bytes = audio.tobytes()

    volume = abs(audio).mean()
    print("volume:",volume)
    speech_detected = volume > 0.05
     
    print("volume:",volume)
    print("speech:",speech_detected)
    print("speech count:",speech_count)
    

    if speech_detected:
        speech_count += 1
    else:
        speech_count = 0

    if speech_count >= SPEECH_THRESHOLD and tts.speaking and (time.time() - last_interrupt_time) > COOLDOWN_SECONDS:
        last_interrupt_time = time.time()
        state = "listening"

        tts.stop()

        output = {
            "interruption": True,
            "action": "pause_tts",
            "state": "listening",
        }

        print(json.dumps(output, indent=4))
        print("Listening mode activated")

        break

    time.sleep(0.05)