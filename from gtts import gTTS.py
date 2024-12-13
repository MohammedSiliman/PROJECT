from gtts import gTTS
from playsound import playsound
from tkinter import *

root = Tk()
root.title("Text to Speech")
root.geometry("400x300")

title_label = Label(root, text="Text to Speech", font=("Arial", 16), fg="blue")
title_label.pack(pady=10)

instruction_label = Label(root, text="Enter your text below:", font=("Arial", 12))
instruction_label.pack(pady=5)

text_entry = Entry(root, width=40, font=("Arial", 12))
text_entry.pack(pady=10)

def convert_and_play():
    text = text_entry.get()
    if text.strip():
        tts = gTTS(text=text)
        tts.save("output.mp3")
        playsound("output.mp3")

def clear_text():
    text_entry.delete(0, END)

def exit_app():
    root.destroy()

button_frame = Frame(root)
button_frame.pack(pady=20)

play_button = Button(button_frame, text="Play", font=("Arial", 12), bg="green", fg="white", command=convert_and_play)
play_button.grid(row=0, column=0, padx=10)

clear_button = Button(button_frame, text="Clear", font=("Arial", 12), bg="blue", fg="white", command=clear_text)
clear_button.grid(row=0, column=1, padx=10)

exit_button = Button(button_frame, text="Exit", font=("Arial", 12), bg="red", fg="white", command=exit_app)
exit_button.grid(row=0, column=2, padx=10)

root.mainloop()