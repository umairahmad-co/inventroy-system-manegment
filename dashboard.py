from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from tkcalendar import DateEntry


#Functionality Part


def employee_form():
    global back_arrow_image
    employee_frame = Frame(window,width=1336,height=700,bg='white')
    #employee_frame=Frame(window,width=1336,height=567,bg='white')
    employee_frame.place(x=200,y=100)
    heading_label=Label(employee_frame,text="Manage Employee Details",font=('times new roman',16,'bold'),bg='#0f4d7d',fg='white')
    heading_label.place(x=0,y=0,relwidth=1)

    # this section is to back arrow icon on Employee Details Page

    back_arrow_image=PhotoImage(file='left-arrow.png')
    back_button=Button(employee_frame,image=back_arrow_image,bd=0,cursor='hand2',bg='white',command=lambda:employee_frame.place_forget())
    back_button.place(x=10,y=30)

    #this section is to set search By on Employee Details Page

    top_frame=Frame(employee_frame,bg='white')
    top_frame.place(x=0, y=60, width=1336, height=290)
    #top_frame.place(x=0,y=60,relwidth=1,relheight=235)
    search_frame=Frame(top_frame,bg='white')
    search_frame.pack()
    search_combobox=ttk.Combobox(search_frame,values=('Id','Name','Email'),font=('times new roman',12),state='readonly',justify='center')
    search_combobox.set('Search By')
    search_combobox.grid(column=0,row=0,padx=20)

    # this section is to set empty field after search button on Employee Details Page

    search_entry=Entry(search_frame,font=('times new roman',12),bg='lightyellow')
    search_entry.grid(column=1,row=0)

    # this section is to set search button on Employee Details Page

    search_button=Button(search_frame,text='Search',font=('time new roman',12),width=10,cursor='hand2',fg='white',bg='#0f4d7d')
    search_button.grid(column=2,row=0,padx=20)

    # this section is to set show all button on Employee Details Page

    show_all_button=Button(search_frame,text='Show All',font=('time new roman',12),width=10,cursor='hand2',
                           fg='white',bg='#0f4d7d')
    show_all_button.grid(column=3,row=0)

    #this section is to set Discription Area on Employee Details Page

    horizontal_scrollbar=Scrollbar(top_frame,orient=HORIZONTAL)
    vertical_scrollbar=Scrollbar(top_frame,orient=VERTICAL)

    employee_treeview=ttk.Treeview(top_frame,columns=('emid','name','email','gender','dob','contact','employee_type','education','work_shift','address','date_of_join','salary','user_type'),show='headings',
                                   yscrollcommand=vertical_scrollbar.set,xscrollcommand=horizontal_scrollbar.set)
    horizontal_scrollbar.pack(side=BOTTOM,fill=X,pady=(0,0))
    vertical_scrollbar.pack(side=RIGHT,fill=Y,pady=(10,0))
    horizontal_scrollbar.config(command=employee_treeview.xview)
    vertical_scrollbar.config(command=employee_treeview.yview)
    employee_treeview.pack(pady=10,padx=10)



    employee_treeview.heading('emid',text='ID')
    employee_treeview.heading('name',text='Name')
    employee_treeview.heading('email',text='Email')
    employee_treeview.heading('gender',text='Gender')
    employee_treeview.heading('dob',text='Date of Birth')
    employee_treeview.heading('contact',text='Contact')
    employee_treeview.heading('employee_type',text='Employee Type')
    employee_treeview.heading('education',text='Education')
    employee_treeview.heading('work_shift',text='Work Shift')
    employee_treeview.heading('address',text='Address')
    employee_treeview.heading('date_of_join',text='Date of Join')
    employee_treeview.heading('salary',text='Salary')
    employee_treeview.heading('user_type',text='User Type')


    employee_treeview.column('emid', width=60, anchor='center')
    employee_treeview.column('name', width=140, anchor='center')
    employee_treeview.column('email', width=180, anchor='center')
    employee_treeview.column('gender', width=80, anchor='center')
    employee_treeview.column('dob', width=100, anchor='center')
    employee_treeview.column('contact', width=100, anchor='center')
    employee_treeview.column('employee_type', width=120, anchor='center')
    employee_treeview.column('education', width=120, anchor='center')
    employee_treeview.column('work_shift', width=100, anchor='center')
    employee_treeview.column('address', width=200, anchor='center')
    employee_treeview.column('date_of_join', width=100, anchor='center')
    employee_treeview.column('salary', width=140, anchor='center')
    employee_treeview.column('user_type', width=140, anchor='center')

    #set te putting value label

    detail_frame=Frame(employee_frame, bg="#f2f2f2")
    detail_frame.place(x=0, y=360, width=1336, height=300)
    #detail_frame.place(x=10,y=370,width=1300, height=300)

    emid_label=Label(detail_frame,text='ID',font=('times new roman',12))
    emid_label.grid(row=0,column=0,padx=20,pady=10,sticky='w')
    emid_entry=Entry(detail_frame,font=('times new roman',12),bg='light yellow')
    emid_entry.grid(row=0,column=1,padx=20,pady=10)

    name_label=Label(detail_frame, text='Name', font=('times new roman', 12))
    name_label.grid(row=0, column=2, padx=20, pady=10,sticky='w')
    name_entry =Entry(detail_frame, font=('times new roman', 12), bg='light yellow')
    name_entry.grid(row=0, column=3, padx=20, pady=10)

    email_label=Label(detail_frame, text='Email', font=('times new roman', 12))
    email_label.grid(row=0, column=4, padx=20, pady=10,sticky='w')
    email_entry= Entry(detail_frame, font=('times new roman', 12), bg='light yellow')
    email_entry.grid(row=0, column=5, padx=20, pady=10)

    gender_label=Label(detail_frame, text='Gender', font=('times new roman', 12))
    gender_label.grid(row=1, column=0, padx=20, pady=10,sticky='w')

    gender_combobox=ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),width=18,state='readonly')
    gender_combobox.set('Select Gender')
    gender_combobox.grid(row=1, column=1)

    dob_label = Label(detail_frame, text='Date of Birth', font=('times new roman', 12))
    dob_label.grid(row=1, column=2, padx=20, pady=10,sticky='w')

    dob_date_entry=DateEntry(detail_frame,width=18, font=('times new roman', 12),state='readonly',date_pattern='dd/MM/yyyy')
    dob_date_entry.grid(row=1, column=3, padx=20, pady=10)

    contact_label = Label(detail_frame, text='Contact', font=('times new roman', 12))
    contact_label.grid(row=1, column=4, padx=20, pady=10,sticky='w')
    contact_entry = Entry(detail_frame, font=('times new roman', 12), bg='light yellow')
    contact_entry.grid(row=1, column=5, padx=20, pady=10)

    employment_type_label = Label(detail_frame, text='Employment Type', font=('times new roman', 12))
    employment_type_label.grid(row=2, column=0, padx=2,pady=10,sticky='w')

    employment_type_combobox = ttk.Combobox(detail_frame, values=('Full Time', 'Part Time','Casual','Contract','Intern'), font=('times new roman', 12), width=18,
                                   state='readonly')
    employment_type_combobox.set('Select Type')
    employment_type_combobox.grid(row=2, column=1)

    education_label = Label(detail_frame, text='Education', font=('times new roman', 12))
    education_label.grid(row=2, column=2, padx=20, pady=10,sticky='w')

    education_options=["B.Tech","B.Com","M.Tech","B.Sc","M.Sc","BBA","MBA","LLB","LLM","B.Arch","M.Arch","F.Sc","Matric"]

    education_combobox = ttk.Combobox(detail_frame, values=education_options, font=('times new roman', 12), width=18,
                                   state='readonly')
    education_combobox.set('Select Education')
    education_combobox.grid(row=2, column=3)

    work_shift_label = Label(detail_frame, text='Work Shift', font=('times new roman', 12))
    work_shift_label.grid(row=2, column=4, padx=20, pady=10,sticky='w')

    work_shift_combobox = ttk.Combobox(detail_frame, values=('Morning', 'Evening','Night'), font=('times new roman', 12), width=18,
                                   state='readonly')
    work_shift_combobox.set('Select Shift')
    work_shift_combobox.grid(row=2, column=5)

    address_shift_label = Label(detail_frame, text='Address', font=('times new roman', 12))
    address_shift_label.grid(row=3, column=0, padx=20, pady=10, sticky='w')
    address_text=Text(detail_frame,width=20,height=2,font=('times new roman', 12),bg='light yellow')
    address_text.grid(row=3, column=1,rowspan=2,sticky="ew",
                  padx=15,
                  pady=10)

    doj_label = Label(detail_frame, text='Date of Joining', font=('times new roman', 12))
    doj_label.grid(row=3, column=2, padx=20, pady=10, sticky='w')

    doj_date_entry = DateEntry(detail_frame, width=18, font=('times new roman', 12), state='readonly',
                               date_pattern='dd/MM/yyyy')
    doj_date_entry.grid(row=3, column=3, padx=20, pady=10)

    user_type_label = Label(detail_frame, text='User Type', font=('times new roman', 12))
    user_type_label.grid(row=4, column=2, padx=20, pady=10, sticky='w')

    user_type_combobox = ttk.Combobox(detail_frame, values=('Admin', 'Employee'),
                                       font=('times new roman', 12), width=18,
                                       state='readonly')
    user_type_combobox.set('Select User Type')
    user_type_combobox.grid(row=4, column=3)

    salary_label = Label(detail_frame, text='Salary', font=('times new roman', 12))
    salary_label.grid(row=3, column=4, padx=20, pady=10, sticky='w')
    salary_entry = Entry(detail_frame, font=('times new roman', 12), bg='light yellow')
    salary_entry.grid(row=3, column=5, padx=20, pady=10)

    password_label = Label(detail_frame, text='Password', font=('times new roman', 12))
    password_label.grid(row=4, column=4, padx=20, pady=10, sticky='w')
    password_entry = Entry(detail_frame, font=('times new roman', 12), bg='light yellow')
    password_entry.grid(row=4, column=5, padx=20, pady=10)















#GUI Part

window = Tk()


window.title("Dashboard")
#window.geometry("1270x668+0+0")
window.geometry("1524x784+0+0")
#window.resizable(0,0)
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
employee_button=Button(left_frame,image= employee_icon,compound=LEFT,text=' Employees',font=('times new roman',20),anchor='w',padx=10,command=employee_form)
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
exit_button=Button(left_frame,image=exit_icon,compound=LEFT,text=' Exit',font=('times new roman',20),anchor='w',padx=10)
exit_button.pack(fill=X)

#<------This is the Total Employees Box on Dashboard ----------->

emp_frame=Frame(window,bg="#2C3E50",bd=3,relief=RIDGE)
emp_frame.place(x=400,y=125,width=250,height=170)

total_emp_icon=PhotoImage(file="total_employee.png")
total_emp_icon_label=Label(emp_frame,image=total_emp_icon,bg="#2C3E50")
total_emp_icon_label.pack(pady=10)

total_emp_label=Label(emp_frame,text='Total Employees',bg="#2C3E50",fg="white",font=('times new roman',15,'bold'))
total_emp_label.pack()

total_emp_count_label=Label(emp_frame,text='0',bg="#2C3E50",fg="white",font=('times new roman',30,'bold'))
total_emp_count_label.pack()

#<------This is the Total Suppliers Box on Dashboard ----------->

sup_frame=Frame(window,bg="#8E44AD",bd=3,relief=RIDGE)
sup_frame.place(x=800,y=125,width=250,height=170)

total_sup_icon=PhotoImage(file="total_sup.png")
total_sup_icon_label=Label(sup_frame,image=total_sup_icon,bg="#8E44AD")
total_sup_icon_label.pack(pady=10)

total_sup_label=Label(sup_frame,text='Total Suppliers',bg="#8E44AD",fg="white",font=('times new roman',15,'bold'))
total_sup_label.pack()

total_sup_count_label=Label(sup_frame,text='0',bg="#8E44AD",fg="white",font=('times new roman',30,'bold'))
total_sup_count_label.pack()

#<------This is the Total Category Box on Dashboard ----------->

cat_frame=Frame(window,bg="#27AE60",bd=3,relief=RIDGE)
cat_frame.place(x=400,y=310,width=250,height=170)

total_cat_icon=PhotoImage(file="total_cat.png")
total_cat_icon_label=Label(cat_frame,image=total_cat_icon,bg="#27AE60")
total_cat_icon_label.pack(pady=10)

total_cat_label=Label(cat_frame,text='Total Category',bg="#27AE60",fg="white",font=('times new roman',15,'bold'))
total_cat_label.pack()

total_cat_count_label=Label(cat_frame,text='0',bg="#27AE60",fg="white",font=('times new roman',30,'bold'))
total_cat_count_label.pack()

#<------This is the Total Products Box on Dashboard ----------->

prod_frame=Frame(window,bg="#2C3E50",bd=3,relief=RIDGE)
prod_frame.place(x=800,y=310,width=250,height=170)

total_prod_icon=PhotoImage(file="total_product.png")
total_prod_icon_label=Label(prod_frame,image=total_prod_icon,bg="#2C3E50")
total_prod_icon_label.pack(pady=10)

total_prod_label=Label(prod_frame,text='Total Products',bg="#2C3E50",fg="white",font=('times new roman',15,'bold'))
total_prod_label.pack()

total_prod_count_label=Label(prod_frame,text='0',bg="#2C3E50",fg="white",font=('times new roman',30,'bold'))
total_prod_count_label.pack()

#<------This is the Total Sales Box on Dashboard ----------->

sales_frame=Frame(window,bg="#E74C3C",bd=3,relief=RIDGE)
sales_frame.place(x=600,y=495,width=250,height=170)

total_sales_icon=PhotoImage(file="total_sales.png")
total_sales_icon_label=Label(sales_frame,image=total_sales_icon,bg="#E74C3C")
total_sales_icon_label.pack(pady=10)

total_sales_label=Label(sales_frame,text='Total Sales',bg="#E74C3C",fg="white",font=('times new roman',15,'bold'))
total_sales_label.pack()

total_sales_count_label=Label(sales_frame,text='0',bg="#E74C3C",fg="white",font=('times new roman',30,'bold'))
total_sales_count_label.pack()



window.mainloop()

