from tkinter import Tk, PhotoImage, Label, Entry, Button
import time
import pygame
import keyboard
import os

count = 2

# init pygame
pygame.init()

# block keys
keyboard.block_key('win')
keyboard.block_key('alt')
keyboard.block_key('ctrl')
keyboard.block_key('esc')
keyboard.block_key('tab')

# os.system('shutdown /s /t 1')
root = Tk()
root.title("Access Required")  # give tile
root.attributes('-fullscreen', True)  # fullscreen
root.resizable(False, False)

# background
back_img = PhotoImage(file="F:\\Python projects\\Windows security system\\img\\Back.png")
label_b = Label(root, image=back_img)
label_b.pack()

# username
label_u = Label(root, font=("Roman", 16), text="Username: ", border=0, bg='black', fg='white')
label_u.place(x=150, y=100)
entry_u = Entry(root, font=("Terminal", 15), border=0)
entry_u.place(x=270, y=100)

# password
label_p = Label(root, font=("Roman", 16), text="Password: ", border=0, bg='black', fg='white')
label_p.place(x=150, y=150)
entry_p = Entry(root, font=("Terminal", 15), border=0, show="*")
entry_p.place(x=270, y=150)


# welcome screen and destroy root and labels
def welcome():
    label_w = Label(root, font=("Arial Black", 30), text="WELCOME ", border=0, bg='black', fg='white')
    label_w.place(x=150, y=150)
    root.update()
    return 0


# create the countdown until shutdown.
def end():
    root.update()
    label_w = Label(root, font=("Arial Black", 30), text="ATTEMPT FAILED\nSYSTEM WILL BE SHUTDOWN IN 5 SECONDS ", border=0, bg='black', fg='white')
    label_w.place(x=150, y=150)
    root.update()
    time.sleep(5)


# destroy labels and create another label
def destruct():
    label_u.destroy()
    entry_u.destroy()
    label_p.destroy()
    entry_p.destroy()
    access_b.destroy()
    root.update()
    return 0


def init_audio():
    pygame.mixer.music.load("F:\\Python projects\\Windows security system\\audio\\010101(init).mp3")
    pygame.mixer.music.play()


def incorrect_audio():
    pygame.mixer.music.load("F:\\Python projects\\Windows security system\\audio\\Access denied(denied).mp3")
    pygame.mixer.music.play()


def end_audio():
    pygame.mixer.music.load("F:\\Python projects\\Windows security system\\audio\\System Shut Down Sound FX (shutdown).mp3")
    pygame.mixer.music.play()
    os.system('shutdown /s /t 1')


def welcome_audio():
    pygame.mixer.music.load("F:\\Python projects\\Windows security system\\audio\\system_activated(after access).mp3")
    pygame.mixer.music.play()


init_audio()
time.sleep(1)


# access button
def access():
    global count
    if entry_u.get() == "Maharshi" and entry_p.get() == "2003@Senmbc":
        destruct()
        welcome()
        welcome_audio()
        time.sleep(3)
        root.destroy()
    else:
        if count != 0:
            count -= 1
            incorrect_audio()
        else:
            destruct()
            end()
            end_audio()


access_i = PhotoImage(file="F:\\Python projects\\Windows security system\\img\\access.png")
access_b = Button(root, image=access_i, command=access, bd=0, bg='black', activeforeground='black', activebackground='black')
access_b.place(x=330, y=220)

root.mainloop()
