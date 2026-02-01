
        import os
import speech_recognition as sr
import datetime

# --- BOLNE WALA FUNCTION (Termux ke liye) ---
def speak(text):
    print(f"Jarvis: {text}")
    # Termux ka apna bolne wala system use karenge
    os.system(f'termux-tts-speak "{text}"')

# --- SUNNE WALA FUNCTION ---
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nChecking background noise... (1 second shant rahein)")
        # Ye line aas-paas ka shor hatati hai
        r.adjust_for_ambient_noise(source, duration=1)
        
        print("Listening... (Ab Boliye)")
        r.pause_threshold = 1  # Rukne ka time
        
        try:
            # 5 second tak wait karega, agar kuch nahi bola to error nahi dega
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Soch raha hoon...")
            query = r.recognize_google(audio, language='en-in')
            print(f"Aapne kaha: {query}")
            
        except Exception as e:
            print("Awaz samajh nahi aayi, phir se boliye...")
            return "None"
            
    return query.lower()

# --- MAIN SYSTEM ---
if __name__ == "__main__":
    speak("Hello Vivek Sir, main online hoon. Boliye kya karna hai?")
    
    while True:
        query = take_command()

        if 'hello' in query:
            speak("Hello Sir! Kaise hain aap?")
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, abhi time hua hai {strTime}")

        elif 'stop' in query or 'bye' in query:
            speak("Goodbye Sir, system closing.")
            break
            
        elif 'none' in query:
            continue
