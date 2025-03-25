from tkinter import *
import wikipedia
import os

window=Tk()

window.geometry("800x400")
window.title("Python Wikipedia")
icon_path=os.path.abspath('wikipedia\wikipedia_icon_TWH_icon.ico')

window.iconbitmap(icon_path)
window.config(bg='white')

def searchfun():
    try:
        query=search.get()
        result=wikipedia.summary(query,sentences=10)
        box.delete('1.0',END)
        box.insert('1.0',result)
    except Exception:
        box.delete('1.0',END)
        box.insert('1.0','No Results Found')



heading=Label(window,text="Python Wikipedia",font=("Arial",20),bg='white')
heading.pack()


search=Entry(window,width=50,borderwidth=5)
search.pack()

searchbtn=Button(window,text="Search",command=searchfun)
searchbtn.pack()

box=Text(window,width=1000,height=300,border=0,font=("Arial",12))
box.pack()

window.mainloop()