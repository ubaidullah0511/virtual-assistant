import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary  



recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com/")
    elif "open twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com/")
    elif "open gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com/")
    elif "what is your name" in command:
        speak("My name is Mini, your virtual assistant.")
    elif command.lower().startswith("play"):
        song = command.replace("play", "").strip().lower()
        if song in musicLibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Sorry, I don't know that song.")
    else:
        speak("Sorry, I didn't understand that command.")

def listen_for_keyword():
    while True:
        with sr.Microphone() as source:
            print("Listening for 'mini' keyword...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=3)

        try:
            recognized_text = recognizer.recognize_google(audio).lower()
            if "mini" in recognized_text:
                speak("Yes?")
                print("Mini activated")
                listen_for_command()
        except sr.RequestError:
            print("Could not request results; check your network connection.")
        except Exception as e:
            print(f"Error: {e}")

def listen_for_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening for command...")
        audio = recognizer.listen(source, timeout=5)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command received: {command}")
        process_command(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that. Please try again.")
    except sr.RequestError:
        print("Could not request results; check your network connection.")
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, there was an error. Please try again.")

if __name__ == "__main__":
    speak("Initializing Mini...")
    listen_for_keyword()
