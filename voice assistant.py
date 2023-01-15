import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the rate of speech
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)

while True:
    # Listen for user input
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Recognize speech and convert to text
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)

        # Perform an action based on the user's command
        if "hello" in text:
            engine.say("Hello there!")
            engine.runAndWait()
        elif "goodbye" in text:
            engine.say("Goodbye!")
            engine.runAndWait()
            break
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Error: {0}".format(e))
