import json
from tkinter import *
from tkinter import ttk

tjson = {"param1":""}

def btn():
    c=entry.get()
    tjson["param1"]=c
    txt = json.dumps(tjson)
    with open("здравствуй.json", "w") as my_file:
        my_file.write(txt)

root = Tk()
root.title("Лучшее приложение")
root.geometry("250x200")

btn = ttk.Button(text="Hello", command=btn)
btn.pack()
entry = ttk.Entry()
entry.pack()
root.mainloop()
