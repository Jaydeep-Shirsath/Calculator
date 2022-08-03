import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print("""     _                 _                 
    | | __ _ _   _  __| | ___  ___ _ __  
 _  | |/ _` | | | |/ _` |/ _ \/ _ \ '_ \ 
| |_| | (_| | |_| | (_| |  __/  __/ |_) |
 \___/ \__,_|\__, |\__,_|\___|\___| .__/ 
             |___/                |_|    
                                              """)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("by Jaydeep")    

speak("Enter Your Number 1")
num1 = int(input("Enter Your Number 1: "))
speak("Enter Your Number 2")
num2 = int(input("Enter Your Number 2: "))
speak(f"Your Number 1 is {num1} and Your Number 2 is {num2}")


print('''
For multiplication press 1: 

''')
print('''For Division press 2:

 ''')
print('''For Subtraction press 3:

 ''')
print("""For Addition press 4: 

""")

speak("For multiplication press 1:, For Division press 2:, For Subtraction press 3:, For Addition press 4:")

speak("Enter Your Fraction Number")
num7 = int(input("Enter Your Fraction Number: "))


if num7 == 1:
    num3 = num1*num2
    print('''
    Your Answer is ''',num3)
    speak(f"Your Answer is {num3}")
elif num7 == 2:
    num6 = num1/num2
    print('''
Your Answer is ''',num6)
    speak(f"Your Answer is {num6}")
elif num7 == 3:
    num5 = num1-num2
    print('''
Your Answer is ''',num5)
    speak(f"Your Answer is {num5}")
else:
    num4=num1+num2
    print('''
Your Answer is ''',num4)
    speak(f"Your Answer is {num4}")
   
print("""
 _____ _                 _          _____            _   _     _             
|_   _| |__   __ _ _ __ | | _____  |  ___|__  _ __  | | | |___(_)_ __   __ _ 
  | | | '_ \ / _` | '_ \| |/ / __| | |_ / _ \| '__| | | | / __| | '_ \ / _` |
  | | | | | | (_| | | | |   <\__ \ |  _| (_) | |    | |_| \__ \ | | | | (_| |
  |_| |_| |_|\__,_|_| |_|_|\_\___/ |_|  \___/|_|     \___/|___/_|_| |_|\__, |
                                                                       |___/ 
""")     
speak("Thanks For Using.")