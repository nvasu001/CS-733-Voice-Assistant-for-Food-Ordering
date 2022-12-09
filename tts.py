import pyttsx3

engine = pyttsx3.init()

while True:
    answer = input("Enter what you want the robot to say: \n")
    engine.say(answer)
    engine.runAndWait()