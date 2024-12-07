""" Importing libraries
 Note: I downloaded/installed most of the library packages via git bash before importing library in my IDE """

import speech_recognition as me # me is the name recognizer
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# creating a listener that recognizer our voice
listener = me.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    
    # A try block that raises an error if the microphone doesn't work and will do nothing if an exception occurs
    try:
        with me.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "merlin" in instruction:
                instruction = instruction.replace('merlin', '')
                print(instruction)

    except:
        pass
    return instruction

def play_Merlin():

    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace('play', "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time' + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date " + date)

    elif 'how are you' in instruction:
        talk('I am fine, how about you')

    elif 'What is your name' in instruction:
        talk('I am Merlin, What can I do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    else:
        talk('Please repeat')
    
play_Merlin()