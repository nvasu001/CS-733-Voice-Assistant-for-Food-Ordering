from vosk import Model, KaldiRecognizer
import pyaudio

model = Model(r'C:\Users\vasud\Desktop\3rd_sem_hw\CS733\CS-733-Voice-Assistant-for-Food-Ordering\CS-733-Voice-Assistant-for-Food-Ordering\vosk-model-small-en-us-0.15') # Read the model
recognizer = KaldiRecognizer(model, 16000)

# Recognize from the microphone

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    #if len(data) == 0:
    #    break

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(text)
        print(text[14:-3])