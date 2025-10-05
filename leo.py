import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    print("Hello Sir! I am Leo. Please tell me how can I help you?")    
    speak("Hello Sir! I am Leo. Please tell me how can I help you?")

def get_news():
    url = 'https://newsapi.org/v2/top-headlines'
    parameters = {
        'apiKey': '904916d47ee6469494c081285cb8f266',  
        'country': 'in',  
    }
    response = requests.get(url, params=parameters)
    news_data = response.json()

    if news_data['status'] == 'ok':
        articles = news_data['articles']
        for index, article in enumerate(articles[:4], start=0):
            title = article['title']
            print(f"News {index + 1}: {title}")
            speak(f"News {index + 1}: {title}")
            time.sleep(2)  
    else:
        speak("Sorry, I couldn't fetch the news at the moment.")
        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'search on google' in query:
            query = query.replace("search on google", "")
            webbrowser.open(f"www.google.co.in/results?search_query={query}")
            
        elif 'close google' in query:
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)  
            if "Google" in pyautogui.getActiveWindowTitle():
                pyautogui.hotkey('ctrl', 'w')  
            else:
                print("Google tab not found.")
        
        elif 'open chrome' in query:
            chrome ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)
        
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
            
        elif 'close youtube' in query:
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)  
            if "Youtube" in pyautogui.getActiveWindowTitle():
                pyautogui.hotkey('ctrl', 'w')  
            else:
                print("Youtube tab not found.")


            
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            
        elif "close gmail" in query:
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)  
            if "Gmail" in pyautogui.getActiveWindowTitle():
                pyautogui.hotkey('ctrl', 'w')  
            else:
                print("Gmail tab not found.")


        elif 'open code' in query:
            codePath = "vs code path\\Code.exe"
            os.startfile(codePath)

        elif 'close code' in query:
            os.system("taskkill /f /im Code.exe")

        #elif 'open spotify' in query:
         #   spotify = "spotify path \\Spotify.exe"
         #   os.startfile(spotify)

        elif 'close spotify' in query:
            os.system("taskkill /f /im Spotify.exe")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            strTime = datetime.date.today()
            print(strTime)
            speak(f"Sir, the date is{strTime}")

        elif 'the day' in query:
            strTime = datetime.datetime.now().strftime("%A")
            print(strTime)
            speak(f"Sir, today is {strTime}")

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "Lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt"  in query:
            os.system("taskkill /f /im cmd.exe")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(10)
                if k==27:
                    break;
            cap.release()
            cv2.imwrite("captured_image.jpg", frame)
            print("Image captured successfully.")
            cv2.imshow("Captured Image", frame)
            cv2.destroyAllWindows()


        elif "go to sleep" in query:
            print(' alright then, I am switching off')
            speak(' alright then, I am switching off')
            sys.exit()

        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listning...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.__truediv__,
                }[op]
            def eval_bianary_expr(op1,oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))
            print(eval_bianary_expr(*(my_string.split())))

        elif "what is my ip address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("your ip adress is")
                speak(ipAdd)
            except Exception as e:
                speak("network is weak, please try again some time later")

        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "refresh" in query:
            pyautogui.hotkey('winleft', 'm')
            pyautogui.hotkey('f5')
            pyautogui.hotkey('winleft','shift' 'm')

        elif "scroll down" in query:
            pyautogui.scroll(1000)

        elif "scroll up" in query:
            pyautogui.scroll(-1000)

        elif 'open paint' in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('paint')
            time.sleep(1)
            pyautogui.press('enter')

        elif "close paint" in query:
            os.system("taskkill /f /im mspaint.exe")

        elif "who are you" in query:
            print('My Name Is Leo')
            speak('My Name Is Leo')
            print('I can Do Everything that my creator programmed me to do')
            speak('I can Do Everything that my creator programmed me to do')

        elif "who created you" in query:
            print('I am created by Somesh, I am created with Python Language, in Visual Studio Code.')
            speak('I am created by Somesh, I am created with Python Language, in Visual Studio Code.')

        elif 'type' in query:
            query = query.replace("type", "")
            pyautogui.write(f"{query}")

        elif 'news update' in query:
            get_news()
