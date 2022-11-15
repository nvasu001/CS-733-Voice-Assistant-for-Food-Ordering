import sys
import threading
import tkinter as tk
import speech_recognition as sr
import pyttsx3 as tts
from neuralintents import GenericAssistant

class Assistant:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 200)
        self.assistant = GenericAssistant("intents.json", intent_methods={"file": self.create_file})
        self.assistant.train_model()
        self.root = tk.Tk()
        self.label = tk.Label(text="🤖",font=("Calibri", 80 , "bold"))
        self.label.pack()
        threading.Thread(target=self.run_assistant).start()
        self.root.mainloop()

    def create_file(self):
        with open("output.txt", "w") as f:
            f.write("Hello world")

    def run_assistant(self):
        while True:
            try:                
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    print(str(text))
                    if "Alex" in str(text):
                        self.label.config(fg="green")

                    audio = self.recognizer.listen(mic)
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    if text == "stop":
                        self.speaker.say("Bye")
                        self.speaker.runAndWait()
                        self.speaker.stop()
                        self.root.destroy()
                        sys.exit()
                    else:
                        if text is not None:
                            response = self.assistant.request(text)
                            if response is not None:
                                self.speaker.say(response)
                                self.speaker.runAndWait()
                        self.label.config(fg="black")

            except sr.WaitTimeoutError():
                print("Error")
                self.label.config(fg="black")
                continue

            except Exception as e: print(e)

Assistant()