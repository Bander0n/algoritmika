import json
from tkinter import *
from tkinter import ttk

with open("Json для проекта.txt", 'r', encoding='utf-8') as my_file:
    data = json.load(my_file)
    
print(json.dumps(data, indent=4, ensure_ascii=False))

citys = []
for element in data:
    if (element["city1"] not in citys):
        citys.append(element["city1"])
    if (element["city2"] not in citys):
        citys.append(element["city2"])
        
#-------------------------------------------------------------------


def click_find():
    k=kuda.get()
    o=otkuda.get()
    for element in data:
        if element["city1"]==k and element["city2"]==o:
            print(element["cost"])
            
                    
#-------------------------------------------------------------------
root = Tk()
root.title("Порты")
root.geometry("700x700")

cos = ['expensive','cheap']
cost = ttk.Combobox(values=cos)
cost.place(height= 30, width = 120,x = 100,y=200)

btn = ttk.Button(text="Найти", command=click_find)
btn.place(x=290, y = 400 ,height = 30, width = 120)

otkuda = ttk.Combobox(values=citys)
otkuda.place(height = 30, width = 120,x = 100,y=100)    

kuda = ttk.Combobox(values=citys)
kuda.place(height = 30, width = 120,x = 500,y=100)

root.mainloop()
