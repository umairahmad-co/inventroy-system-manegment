from tkinter import *

window = Tk()


window.title("Dashboard")
window.geometry("1270x668+0+0")
#window.geometry("1524x784+0+0")
window.resizable(0,0)
window.configure(bg="white")

bg_image= PhotoImage(file="logo.png")
title_label = Label(window,image=bg_image,compound=LEFT, text="Inventory Manegment System", fg="white", bg="#010c48",anchor='w',padx=20,font=("times new roman",20,'bold'))
title_label.place(x=0,y=0,relwidth=1)

#<------This is the Logout Button on Dashboard ----------->
logoutButton = Button(window,text="Logout",font=("times new roman",20,'bold'),fg='#010c48')
logoutButton.place(x=1300,y=10)


#<------This is the Subtitle row on Dashboard ----------->
sub_title_label=Label(window,text="Welcome Admin\t\t Date: 23-06-2026\t\t Time: 08:40:17 pm",font=("times new roman",15,'bold'),bg='#4d636d',fg='white')
sub_title_label.place(x=120,y=10)
sub_title_label.place(x=0,y=70,relwidth=1)

#<------This Sidebar Section on Dashboard ----------->
left_frame=Frame(window)
left_frame.place(x=0,y=102,width=200,height=755)


logoImage=PhotoImage(file="checklist.png")
image_label=Label(left_frame,image=logoImage)
image_label.place(x=120,y=0,relwidth=1)
image_label.grid(row=0,column=0)
image_label.pack()

menu_label=Label(left_frame,text='Menu',font=('times new roman',20),bg='#009688')
menu_label.pack(fill=X)

employee_icon=PhotoImage(file="employee-card.png")
employee_button=Button(left_frame,image= employee_icon,compound=LEFT,text=' Employees',font=('times new roman',20),anchor='w',padx=10)
employee_button.pack(fill=X)

supplier_icon=PhotoImage(file="supplier.png")
supplier_button=Button(left_frame,image=supplier_icon,compound=LEFT,text=' Suppliers',font=('times new roman',20),anchor='w',padx=10)
supplier_button.pack(fill=X)

category_icon=PhotoImage(file="categories.png")
category_button=Button(left_frame,image=category_icon,compound=LEFT,text=' Categories',font=('times new roman',20),anchor='w',padx=10)
category_button.pack(fill=X)

product_icon=PhotoImage(file="product.png")
product_button=Button(left_frame,image=product_icon,compound=LEFT,text=' Products',font=('times new roman',20),anchor='w',padx=10)
product_button.pack(fill=X)

sale_icon=PhotoImage(file="sale.png")
sale_button=Button(left_frame,image=sale_icon,compound=LEFT,text=' Sales',font=('times new roman',20),anchor='w',padx=10)
sale_button.pack(fill=X)

exit_icon=PhotoImage(file="exit.png")
exit_button=Button(left_frame,image=exit_icon,compound=LEFT,text=' exit',font=('times new roman',20),anchor='w',padx=10)
exit_button.pack(fill=X)

#<------This is the Total Employees Box on Dashboard ----------->

emp_frame=Frame(window,bg="#2C3E50",bd=3,relief=RIDGE)
emp_frame.place(x=400,y=125,width=250,height=170)

total_emp_icon=PhotoImage(file="total_employee.png")
total_emp_icon_label=Label(emp_frame,image=total_emp_icon,bg="#2C3E50")
total_emp_icon_label.pack()

total_emp_label=Label(emp_frame,text='Total Employees',bg="#2C3E50",fg="white",font=('times new roman',15,'bold'))
total_emp_label.pack()

total_emp_count_label=Label(emp_frame,text='0',bg="#2C3E50",fg="white",font=('times new roman',30,'bold'))
total_emp_count_label.pack()

#<------This is the Total Suppliers Box on Dashboard ----------->

sup_frame=Frame(window,bg="#2C3E50",bd=3,relief=RIDGE)
sup_frame.place(x=800,y=125,width=250,height=170)

total_sup_icon=PhotoImage(file="total_sup.png")
total_sup_icon_label=Label(sup_frame,image=total_sup_icon,bg="#2C3E50")
total_sup_icon_label.pack()

total_emp_label=Label(sup_frame,text='Total Suppliers',bg="#2C3E50",fg="white",font=('times new roman',15,'bold'))
total_emp_label.pack()

total_emp_count_label=Label(sup_frame,text='0',bg="#2C3E50",fg="white",font=('times new roman',30,'bold'))
total_emp_count_label.pack()







window.mainloop()

