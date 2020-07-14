import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_hear = speech_recognition.Recognizer()
robot_say = pyttsx3.init()
robot_brain = ""

print("Robot: I'm listening")
robot_say.say("I'm listening")
robot_say.runAndWait()


while True:
    # Robot hear
    with speech_recognition.Microphone() as mic:
        audio = robot_hear.listen(mic)

    print("Robot:...")

    try:
        you = robot_hear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    # Robot think
    if you == "":
        robot_brain = "I can here you, please try again"
    elif "hello" in you:
        robot_brain = "hello!"
    elif "today" in you:
        today = date.today()
        robot_brain = ("Today is: " + today.strftime("%B %d, %Y"))
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minute")
    elif "bye" in you:
        robot_brain = "Goodbye, have a nice day"
        print("Robot: " + robot_brain)
        # Robot said
        robot_say.say(robot_brain)
        robot_say.runAndWait()
        print("Shutting down...")
        break
    else:
        robot_brain = "Everything fine, thanks and you"

    print("Robot: " + robot_brain)

    # Robot said

    robot_say.say(robot_brain)
    robot_say.runAndWait()

    #DrQA de xay dung tiep