
import sys
sys.path.append('path if not correct')


from gtts import gTTS
import os
import playsound
import json  
import PySimpleGUI as sg

sg.theme('DarkTeal9')

layout = [
    [sg.Text('Enter the message: ')],
    [sg.Text('Message', size=(30,3)), sg.InputText(key='')],
    [sg.Submit(), sg.Exit()]
        ]
window = sg.Window('Simple data entry form', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        language = 'sv'   # en, da, sv,
        s = json.dumps(values)
        print(s)
        myobj = gTTS(text=s, lang=language, slow=False)
        myobj.save("tt.mp3")
        playsound.playsound("tt.mp3")
        os.remove("tt.mp3")
window.close()




