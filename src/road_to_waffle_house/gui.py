from src.road_to_waffle_house.distance_matrix import run
import src.road_to_waffle_house.distance_matrix as distance_matrix 

"""
Giving credit where it is due
I coded a lot of the base design like the windows, grids, etc...
ChatGPT did the window resizing aspect to allow for the program to resize effortlessly
between windowed mode and windowed fullscreen.

So, this block comment is to give credit for that feature, and whatever comments and code fixes
ChatGPT took upon itself to make for the GUI to work as I intend. - Justin Miles
"""

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import pygame
import time
import threading

# Function starts the gui
def start_gui(run_loop=True):
    global main_window
    main_window = tk.Tk()
    main_window.title("How far are you from Waffle House?")
    main_window.geometry("800x600")
    main_window.configure(bg="black")

    # Load the image (replace with your image file path)
    image = Image.open("photos/wafflehouse.png")  # e.g., "wafflehouse.png"
    image = image.resize((600, 400), Image.Resampling.LANCZOS)  # Resize to smaller dimensions
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(main_window, image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.pack(expand=True)

    # Add a button underneath the image
    global start_button
    start_button = tk.Button(main_window, text="Click Me!", font=("Helvetica", 14),width=45,height=5,bg="yellow",command=open_prompt_window)
    start_button.pack(pady=50)

    threading.Thread(target=play_audio, daemon=True).start()

    main_window.mainloop()

def open_prompt_window():
    start_button.destroy()
    global prompt_window
    prompt_window =tk.Tk()

    prompt_window.title("Location Prompt")
    prompt_window.geometry("400x250")
    prompt_window.configure(bg="black")
    prompt_window.resizable(False, False)

    center_frame = tk.Frame(prompt_window,bg="black")
    center_frame.pack(fill="both", expand=True)  # Use expand to push to center

    prompt = tk.Label(center_frame, font=("Helvetica", 14), text="Please enter an address with state abbreviation",bg="black",fg="yellow")
    prompt.pack(pady=40)

    global entry
    entry = tk.Entry(center_frame, font=("Helvetica", 14), width=25, bg="gray", fg="yellow")
    entry.pack(pady=5)

    submit_button = tk.Button(center_frame, text="Submit", bg="gray", fg="yellow", command=on_submit)
    submit_button.pack(pady=20)

     # Error label that will display invalid input message (initially empty)
    global error_label
    error_label = tk.Label(center_frame, text="", bg="black", fg="red", font=("Helvetica", 12))
    error_label.pack(pady=5)

    prompt_window.mainloop()

def on_submit():
        user_input = entry.get()

        if user_input == "":
            error_label.config(text="Invalid input")
            return
        
        info = run(user_input)
        print(distance_matrix.done)
        if distance_matrix.done == False:
            error_label.config(text="Invalid input")
        else:
            prompt_window.after(100, open_final_window(info))
            
def setup_audio():
    pygame.mixer.init()
    sound1 = pygame.mixer.Sound("audio/ambiance.mp3")
    sound1.set_volume(1.0)
    sound2 = pygame.mixer.Sound("audio/waffle.mp3")
    sound2.set_volume(0.2)
    return sound1, sound2

def play_audio_repeatedly(sound):
    while True:
        print("Ambiance played!")
        sound.play()
        time.sleep(10)

def play_audio():
    sound1, sound2 = setup_audio()
    sound1.play()
    play_audio_repeatedly(sound2)

def open_final_window(info):
    print("INFO:", info)
    
    # Destroy previous windows
    main_window.destroy()
    prompt_window.destroy()

    # Create a new window
    final_window = tk.Tk()
    final_window.title("How far are you from Waffle House?")
    final_window.geometry("800x600")  # Window size, adjust if necessary
    final_window.configure(bg="black")

    # Frame for organizing the content
    frame = tk.Frame(final_window, bg="black")
    frame.pack(fill="both", expand=True)

    # Load the first image (above the text)
    image = Image.open("photos/you_are.png")  # Adjust path if needed
    image = image.resize((300, 200), Image.Resampling.LANCZOS)  # Resize the image smaller
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the first image
    image_label = tk.Label(frame, image=photo, bg="black")
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.pack(pady=10)

    # Create text labels for the information
    error_label1 = tk.Label(frame, text=f"{info[0]}", bg="black", fg="yellow", font=("Helvetica", 14))
    error_label2 = tk.Label(frame, text=f"{info[1]}", bg="black", fg="yellow", font=("Helvetica", 14))

    # Pack the text labels below the first image
    error_label1.pack(pady=5)
    error_label2.pack(pady=5)

    # Load the second image (below the text)
    image_bottom = Image.open("photos/from.png")  # Adjust path if needed
    image_bottom = image_bottom.resize((200, 150), Image.Resampling.LANCZOS)  # Resize the image smaller
    photo_bottom = ImageTk.PhotoImage(image_bottom)

    # Create a label to display the second image (below the text)
    image_label_bottom = tk.Label(frame, image=photo_bottom, bg="black")
    image_label_bottom.image = photo_bottom  # Keep a reference to avoid garbage collection
    image_label_bottom.pack(pady=10)

    # Load the third image (below the second image)
    image_bottom2 = Image.open("photos/logo.png")  # Adjust path if needed
    image_bottom2 = image_bottom2.resize((300, 150), Image.Resampling.LANCZOS)  # Resize the image bigger
    photo_bottom2 = ImageTk.PhotoImage(image_bottom2)

    # Create a label to display the third image (below the second image)
    image_label_bottom2 = tk.Label(frame, image=photo_bottom2, bg="black")
    image_label_bottom2.image = photo_bottom2  # Keep a reference to avoid garbage collection
    image_label_bottom2.pack(pady=10)

    # Start the final window's main loop
    final_window.mainloop()


