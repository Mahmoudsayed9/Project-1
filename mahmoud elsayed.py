import tkinter as tk
from gtts import gTTS
import playsound
import os

def text_to_speech():
    text = entry.get()
    if text.strip():
        audio_file = "speech.mp3"
        try:
            tts = gTTS(text=text, lang='en')
            tts.save(audio_file)
            playsound.playsound(audio_file)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            if os.path.exists(audio_file):
                os.remove(audio_file)
    else:
        print("Please enter text to convert.")

def clear_text():
    entry.delete(0, tk.END)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Text to Speech Project")
root.geometry("600x500")
root.configure(bg="white")

label = tk.Label(root, text="Text to Speech Project", font=("Arial", 16, "bold"), bg="white", fg="black")
label.pack(pady=20)

entry = tk.Entry(root, width=40, font=("Arial", 14), bd=2, bg="lightgrey", fg="black")
entry.pack(pady=10, padx=20)
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=5)

play_button = tk.Button(button_frame, text="Play", command=text_to_speech, bg="black", fg="white", width=12, height=2)
play_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_text, bg="blue", fg="white", width=12, height=2)
clear_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(button_frame, text="Exit", command=exit_app, bg="red", fg="white", width=12, height=2)
exit_button.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
root.mainloop()