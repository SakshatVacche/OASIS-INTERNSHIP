import speech_recognition as sr
import datetime
import webbrowser

def greet():
    return "Hello! How can I assist you today?"

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    return f"The current time is {current_time}"

def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"Today's date is {current_date}"

def search_web(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    return f"Searching the web for {query}"

def voice_assistant(command):
    if "hello" in command.lower():
        return greet()
    elif "time" in command.lower():
        return get_time()
    elif "date" in command.lower():
        return get_date()
    elif "search" in command.lower():
        query = command.split("search", 1)[1].strip()
        return search_web(query)
    else:
        return "I'm sorry, I don't understand that command."

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            response = voice_assistant(command)
            print(response)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestError as e:
            print(f"Error making the request: {e}")

if __name__ == "__main__":
    main()
