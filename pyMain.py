# mood metre using tKinter
# 0.3
import tkinter as tk
from tkinter import ttk
import time
from functools import partial
from os import system

window = tk.Tk()
file = open("C:/Users/StG_44/Desktop/Projects/MoodMeter/moods.log", "a")

def clear():
    system("cls")

def on_click(text):
    newString = "[{0}, {1}]\n".format(time.ctime(), text)
    print("returning::Debug::newString: " + str(newString))
    file.write(newString)

## I'll need to use 2D arrays for this since the grid math won't work, so treat them more like coords ig
# array of colors for buttons from left --> right
colorArr = [["#842919", "#c56040", "#d96c60", "#e09866", "#ebc077", "#f2e080",],
            ["#842919", "#c56040", "#d96c60", "#e09866", "#ebc077", "#f2e080", ],
            ["#842919", "#c56040", "#d96c60", "#e09866", "#ebc077", "#f2e080", ],
            ["#758ea1", "#96adc4", "#d2dde5", "#c8cea6", "#a6ab87", "#6f794d", ],
            ["#758ea1", "#96adc4", "#d2dde5", "#c8cea6", "#a6ab87", "#6f794d", ],
            ["#758ea1", "#96adc4", "#d2dde5", "#c8cea6", "#a6ab87", "#6f794d"]]

# array of moods from left --> right
moodArr = [["Genuine Threat to Society", "(In Minecraft)", "Goblin Mode", "Silly Goose", "Let's Go", "LET'S FUCKING GOOOOOOO", ],
           ["You've Gotta be Fucking Kidding Me", "FUCK", "Fuck it We Ball", "Bitches Love my Moustache", "We're So Back", "We're So Fucking Back", ],
           ["I Hate Women", "We Ain't Making It Out of the Hood", "*Internal Screaming*", "It Is What it Is", "We're Gonna Make it Bro", "Modelo Time", ],
           ["Tiredness That Sleepy Won't Fix", "It's Just One of Those Days...", "yeah bro, I just need some sleep", "It really do be like that sometimes", "Straight Chilling", "'neat'", ],
           ["Mom Would be Sad", "It's So Over", "This Time I'm Really Gonna Do It", "Anotha Day, Anotha Dolla", "'cool'", "We Vibin", ],
           ["[x]", "My Dog Wouldn't Understand", "One Day Something Will Kill Me", "Comfortably Numb", "'aight'", "Bing Chilling"]]

btn = [] # list that stores the button int IDs

## frameL
for i in range(6):
    for j in range(6):
        frameL = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frameL.grid(row=i, column=j)
        button = tk.Button(master=frameL, text=moodArr[i][j], width=25, height=10, bg=colorArr[i][j], fg="black", command=partial(on_click, moodArr[i][j]))
        button.pack(side=tk.LEFT)


## event loop runner
window.mainloop()