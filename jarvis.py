import os
import json
import time

# --- BOLNE WALA SYSTEM ---
def speak(text):
    print(f"Vivek: {text}")
    # Termux ko bulwane ka command
    os.system(f"termux-tts-speak '{text}'")

# --- SUNNE WALA SYSTEM ---
def listen():
    print("\nListening... (Bolne ke baad back karein)")
    # Mic khulega
    text = os.popen("termux-speech-to-text").read().strip().lower()
    # Screen par dikhayega ki kya suna (Debugging ke liye)
    if text:
        print(f"--> Suna: {text}")
    return text

# --- MAIN LOGIC ---
os.system("clear")
print("--- VIVEK SYSTEM READY ---")
speak("Main taiyaar hoon. Boliye Vivek On.")

is_awake = False

while True:
    try:
        text = listen()
        
        if not text:
            continue

        # --- 1. ON/OFF CONTROL ---
        if "vivek on" in text or "wake up" in text or "start" in text:
            is_awake = True
            speak("Online hoon sir. Boliye.")
            continue
        
        elif "vivek off" in text or "sleep" in text:
            is_awake = False
            speak("Main offline ja raha hoon.")
            continue

        # Agar System So raha hai toh ignore karega
        if is_awake == False:
            continue

        # --- 2. COMMANDS (Jab wo jaaga ho) ---

        # OPEN APP
        if "open" in text:
            app_name = text.replace("open", "").strip().replace(" ", "")
            speak(f"Opening {app_name}")
            os.system(f"termux-open-url https://{app_name}.com")

        # CLOSE APP
        elif "close app" in text:
            speak("Closing app")
            os.system("cmd input keyevent 3")

        # CALL
        elif "call" in text:
            name = text.replace("call", "").strip()
            speak(f"Calling {name}")
            try:
                contact_list = json.loads(os.popen("termux-contact-list").read())
                for contact in contact_list:
                    if name in contact.get("name", "").lower():
                        os.system(f"termux-telephony-call {contact.get('number')}")
                        break
            except:
                speak("Contact nahi mila.")

        # CUT CALL
        elif "cut" in text:
            speak("Call kaat raha hoon")
            os.system("cmd input keyevent 6")

        # PLAY MUSIC
        elif "play" in text:
            song = text.replace("play", "").strip()
            query = song.replace(" ", "+")
            speak(f"Playing {song}")
            os.system(f"termux-open-url https://music.youtube.com/search?q={query}")

        # CLOSE MUSIC
        elif "close music" in text:
            speak("Music band kar raha hoon")
            os.system("cmd input keyevent 86") # Stop
            time.sleep(1)
            os.system("cmd input keyevent 3")  # Home

        # Agar kuch ulta seedha suna
        else:
            print("Command samajh nahi aaya, dubara boliye.")

    except KeyboardInterrupt:
        break
