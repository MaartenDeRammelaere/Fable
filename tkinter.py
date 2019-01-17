import tkinter as tk
    

def write_slogan():
    print("Dit kan een pop up geven over hoe dit programma te gebruiken")
    
def say_yeet():
    print("Dit kan een programma worden")
    
def say_yote():
    print("Dit kan een tweede programma zijn")
    

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="close", fg="red", command=quit)
button.pack(side=tk.BOTTOM)

slogan = tk.Button(frame, text="Hello", command=write_slogan)
slogan.pack(side=tk.TOP)

yeet = tk.Button(frame, text="Programma", command=say_yeet)
yeet.pack(side=tk.TOP)

yote = tk.Button(frame, text="Programma 2", command=say_yote)
yote.pack(side=tk.TOP)

root.mainloop()