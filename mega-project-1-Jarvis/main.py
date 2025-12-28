import speech_recognition as sr
import webbrowser
import pyttsx3

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    
    while True:
        # Listen for the word "Jarvis"
        # Obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # recognize speech using Sphinx
        try:
            command = r.recognize_google(audio)
            print(f"Google thinks you said {command}")
        except sr.UnknownValueError:
            print("Google could not understand audio")
        except sr.RequestError as e:
            print("Google error; {0}".format(e))