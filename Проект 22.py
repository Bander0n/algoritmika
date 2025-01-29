import json
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Порты")
root.geometry("700x700")

tjson = {"param1,":"", "param2,":"","param3,":"","param4,":"","param5,":""}
citys = ["s", "r", "a", "c"]


def btn():
    a=otkuda.get()
    b=kuda.get()
    c=cost.get()
    d=company.get()
    e=hall1.get()
    tjson["param1"]=a
    tjson["param2"]=b
    tjson["param3"]=c 
    tjson["param4"]=d
    tjson["param5"]=e
    txt = json.dumps(tjson)
    with open("здравствуй.json", "w") as my_file:
        my_file.write(txt + '\n')
        my_file.close()
otkuda = ttk.Combobox(values=citys)
otkuda.place(height = 30, width = 120,x = 100,y=100)    

kuda = ttk.Combobox(values=citys)
kuda.place(height = 30, width = 120,x = 500,y=100)


cos = ['+','-']
cost = ttk.Combobox(values=cos)
cost.place(height= 30, width = 120,x = 100,y=200)


comp = ['company','company1']
company = ttk.Combobox(values=comp)
company.place(height = 30, width = 120,x = 500,y=200)

hall1 = ttk.Entry()
hall1.place(x=290, y = 300 ,height = 30, width = 120)
hall1.pack()



btn = ttk.Button(text="Посчиать",command = btn)
btn.place(x=290, y = 400 ,height = 30, width = 120)

 
root.mainloop()



























