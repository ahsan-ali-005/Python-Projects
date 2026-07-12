import webbrowser
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from google import genai
from google.genai import types

class Jarvis:
    def __init__(self):
        self.tasks = {
            "open youtube": "https://youtube.com/",
            "open wikipedia": "https://www.wikipedia.org/",
            "open instagram": "https://instagram.com/",
            "open coursera": "https://coursera.org"
        }
        
        load_dotenv()
        
        self.client = genai.Client()
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

    def speak(self, text):
        print(text)
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def run(self):
        self.speak("Hey, Jarvis here. How can I assist you, Sir?")

        while True:
            text = self.get_input()

            if not text:
                continue

            text = text.lower()

            if "stop jarvis" in text:
                self.speak("Stopping... Exiting now.")
                break

            if text == "jarvis":
                self.speak("Yes Sir")
                continue

            if self.execute_manual_tasks(text):
                continue

            answer = self.ask_genai(text)
            if answer:
                self.speak(answer)

    def get_input(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

            try:
                return self.recognizer.recognize_google(audio, language="en-US")
            except sr.UnknownValueError:
                print("Sorry, speech not recognized.")
            except sr.RequestError:
                print("Speech recognition service unavailable.")
            
            return None

    def execute_manual_tasks(self, text):
        for task, url in self.tasks.items():
            if task in text:
                self.speak(f"Opening {task.replace('open ', '')}")
                webbrowser.open(url)
                return True
        return False

    def ask_genai(self, prompt):
        try:
            response = self.client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction="Keep the answer concise and to the point"
                )
            )
            return response.text
        except Exception as e:
            print(f"Error communicating with AI: {e}")
            return "I am having trouble connecting to my core processing unit."

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()