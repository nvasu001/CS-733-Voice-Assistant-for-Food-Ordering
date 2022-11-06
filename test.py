import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.25)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"{text}")
            
    except sr.UnknownValueError():
        recognizer = sr.Recognizer()
        continue
    
    except sr.WaitTimeoutError():
        recognizer = sr.Recognizer()
        continue