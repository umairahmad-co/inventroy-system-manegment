from tkinter import *

window = Tk()


window.title("Dashboard")
window.geometry("1270x668+0+0")
window.resizable(0,0)
window.configure(bg="white")

bg_image= PhotoImage(file="logo.png")
title_label = Label(window,image=bg_image,compound=RIGHT, text="Inventory Manegment System", fg="white", bg="#010c48",anchor='w',padx=20,font=("times new roman",40,'bold'))
title_label.place(x=0,y=0,relwidth=1)

logoutButton = Button(window,text="Logout",command=window.quit)

window.mainloop()

