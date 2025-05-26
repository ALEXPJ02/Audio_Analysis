# Author: Alexandro Jauregui
import sounddevice as sd
import numpy as np
import os
import wave

def play_audio(signal, sample_rate=48000):
    sd.play(signal, sample_rate)
    sd.wait()

def record_audio(duration=5.0, sample_rate=48000, channels=1):
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='float32')
    sd.wait()
    print("Recording complete.")
    return audio.flatten()

def save_wav(filename, data, sample_rate=48000):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    scaled = np.int16(data / np.max(np.abs(data)) * 32767)
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(scaled.tobytes())

def load_wav(filename):
    with wave.open(filename, 'rb') as wf:
        sample_rate = wf.getframerate()
        frames = wf.readframes(wf.getnframes())
        data = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32767.0
    return data, sample_rate
