from tkinter import *

window = Tk()


window.title("Dashboard")
window.geometry("1524x784+0+0")
window.resizable(0,0)
window.configure(bg="white")

bg_image= PhotoImage(file="logo.png")
title_label = Label(window,image=bg_image,compound=LEFT, text="Inventory Manegment System", fg="white", bg="#010c48",anchor='w',padx=20,font=("times new roman",20,'bold'))
title_label.place(x=0,y=0,relwidth=1)

logoutButton = Button(window,text="Logout",font=("times new roman",20,'bold'),fg='#010c48')
logoutButton.place(x=1300,y=10)

sub_title_label=Label(window,text="Welcome Admin\t\t Date: 23-06-2026\t\t Time: 08:40:17 pm",font=("times new roman",15,'bold'),bg='#4d636d',fg='white')
sub_title_label.place(x=120,y=10)
sub_title_label.place(x=0,y=70,relwidth=1)

left_frame=Frame(window)
left_frame.place(x=0,y=102,width=200,height=755)

logoImage=PhotoImage(file="checklist2.png")
image_label=Label(left_frame,image=logoImage)
image_label.place(x=120,y=0,relwidth=1)
image_label.grid(row=0,column=0)





window.mainloop()

