from tkinter import *

window = Tk()


window.title("Dashboard")
window.geometry("1270x668+0+0")
window.resizable(0,0)
window.configure(bg="white")

bg_image= PhotoImage(file="logo.png")
title_label = Label(window,image=bg_image,compound=LEFT, text="Inventory Manegment System", fg="white", bg="#010c48",font=("times new roman",40,'bold'))
title_label.place(x=0,y=0)



window.mainloop()

