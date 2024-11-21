import tkinter as tk
import pygame

# Creating a function to play the .mp3 file
def play_sound():
    pygame.mixer.music.play()

# Starting the pygame mixer
pygame.mixer.init()

# Staging the sound to be played by loading the .mp3 file
sound_file = "./LeeroyJenkins.mp3"
pygame.mixer.music.load(sound_file)

# Creating the main screen that will contain the button to press to play the sound
root = tk.Tk()
root.title("Leeroy Jenkins Button")
button = tk.Button(root, text="LEEROY JENKINS!",font=("Helvetica",20), command=play_sound)
button.pack()

# Run the tkinter event loop
root.mainloop()