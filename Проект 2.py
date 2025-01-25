import json
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Лучшее приложение")
root.geometry("250x200")

tjson = {"param1,":"", "param2,":""}

def btn2():
    a=entry1.get()
    b=entry2.get()
    tjson["param1"]=a
    tjson["param2"]=b
    txt = json.dumps(tjson)
    with open("здравствуй.json", "a") as my_file:
        my_file.write(txt + '\n')
        my_file.close()
        with open("здравствуй.json", "r") as file:
            for line in file:
                print(line + '\n')

entry1 = ttk.Entry()
entry1.pack()

entry2 = ttk.Entry()
entry2.pack()

btn2 = ttk.Button(text="обработать", command=btn2)
btn2.place(relx=0.1,rely=10,width=110,height=70)
btn2.pack()




































