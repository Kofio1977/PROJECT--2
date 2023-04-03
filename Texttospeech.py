import pyttsx3
import PySimpleGUI as sg


# Create the PySimpleGUI window layout
layout = [[sg.Text("Enter text to convert to speech:")],
          [sg.InputText(key="-INPUT-"), sg.Button("Speak")],
          [sg.Text('Select Voice type'),sg.Radio("Male voice", "RADIO1", default=True, key="-MALE-"), sg.Radio("Female voice", "RADIO1", key="-FEMALE-")],
          [ sg.Button("Exit")]]

# Create the PySimpleGUI window
window = sg.Window("Text to Speech Converter", layout)

# Create the pyttsx3 engine
engine = pyttsx3.init()

# Define the speak function to convert text to speech
def speak(text, male=True):
    voices = engine.getProperty("voices")
    if male:
        voice = voices[0]
    else:
        voice = voices[1]
    engine.setProperty("voice", voice.id)
    engine.say(text)
    engine.runAndWait()

# Event loop to process PySimpleGUI events
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Speak":
        text = values["-INPUT-"]
        male = values["-MALE-"]
        speak(text, male)

# Close the PySimpleGUI window
window.close()
