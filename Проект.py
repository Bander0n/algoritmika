import json
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Лучшее приложение")
root.geometry("250x200")



tjson = {"param1":""}

def btn():
    c=entry.get()
    tjson["param1"]=c
    txt = json.dumps(tjson)
    with open("здравствуй.json", "a") as my_file:
        my_file.write(txt)
        
bjson = {"param2":""}

def btn1():
    b=entry.get()
    bjson["param2"]=b
    txt = json.dumps(bjson)
    with open("здравствуй.json", "a") as my_file:
        my_file.write(txt)


btn = ttk.Button(text="обработать", command=btn)
btn.pack
btn.place(relx=0.1,rely=1,width=110,height=70)
entry = ttk.Entry()
entry.pack()


btn1 = ttk.Button(text="обработать", command=btn1)
btn1.place(relx=0.1,rely=0.1,width=110,height=70)
btn1.pack()
entry = ttk.Entry()
entry.pack()
root.mainloop()
