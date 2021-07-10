#main tkinter file

import tkinter
from tkinter import *
import mailtask  
import usertasks
import tkinter.messagebox


main = tkinter.Tk()
main.title("TODO")
main.geometry("500x700")
main.resizable(True, True)


background_image=tkinter.PhotoImage(file="download.png")
background_label = tkinter.Label(main, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


email_var=tkinter.StringVar()
subject_var=tkinter.StringVar()
message_var=tkinter.StringVar()

#populate function updates the list-box with the data in the database
def populate():
    listbox.delete(0, END)
    for rows in usertasks.show():
        listbox.insert(END, rows)

#delete functon to delete the task in the list-box
def deletetask(event):
    usertasks.deletebytask(listbox.get(ANCHOR))
    populate()


#run function to run all the tasks using mailtask.py file
def run():
    c=0
    for rows in usertasks.show():
        listbox.itemconfig(c,{'fg':'orange'})
        try:
            mailtask.send_email(rows[0],rows[1],rows[2])
            listbox.itemconfig(c,{'fg':'green'})
            c+=1
            try:
                listbox.itemconfig(c,{'fg':'orange'})
            except:
                pass
            tkinter.messagebox.showinfo("Greetings",  "Hey dear, email sent to "+rows[0])
            print("Message sent to "+rows[0])
        except:
            listbox.itemconfig(c,{'fg':'yellow'})
            c+=1
            try:
                listbox.itemconfig(c,{'fg':'orange'})
            except:
                pass
            tkinter.messagebox.showinfo("Error",  "Please check your internet connection or Reciever Email")
            print("Message not sent to "+rows[0])


#submit function to submit user data to the database
def submit():
    email=email_var.get()
    subject =subject_var.get()
    message = message_var.get()
    usertasks.insertdata(email,subject,message)
    email_var.set("")
    subject_var.set("")
    message_var.set("")
    populate()
    usertasks.show()
    

email = Label(main,
     text="Email", 
     background="#49A",
     foreground="#ffffff",
     font=("Calibri", 12),
     width =10,).pack(pady=5)
E1 = Entry(main,textvariable = email_var,bd =5,width=50).pack(pady=5)

subject = Label(main,
        text = "Subject",
        background="#49A",
        foreground="#ffffff",
        font=("Calibri", 12),
        width =10).pack(pady=5)
E2 = Entry(main,textvariable = subject_var, bd =5,width=50).pack(pady=5)

message = Label(main,
        text = "Message",
        background="#49A",
        foreground="#ffffff",
        font=("Calibri", 12),
        width =10).pack(pady=5)
E2 = Entry(main,textvariable = message_var, bd =5,width=50).pack(pady=5)


submit = Button(main,
         text = "Add Task",
         background="#FFDAB9",
         foreground="#000000",
         font=("Calibri", 13),
         width =12,
         command=submit).pack(pady=5) 


tkinter.Label(
    main,
    text="All Tasks",
    background="#49A",
    foreground="#ffffff",
    font=("Calibri", 14),
    width =12,).pack(pady=10)

taskframe = tkinter.Frame(
    main,
    bg="#1d1d1d",
)
taskframe.pack(fill=BOTH, expand=500)
scrollbar = Scrollbar(taskframe)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(
          taskframe,
          font=("Verdana 10 bold"),
          bg="#1d1d1d",
          fg="red",)
listbox.pack(fill=BOTH, expand=300)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

tkinter.Button(main,
             text = "Run Tasks",
             background="#FFDAB9",
             foreground="#000000",
             font=("Calibri", 13),
             width =12,
             command=run).pack(pady=10) 

listbox.bind("<Double-Button-1>", deletetask)
populate()

tkinter.Label(
    main,
    text="TIP : Double Click on task to Delete Task",
    width=50,
    background="#1d1d1d",
    foreground="#ADD8E6",
    font=("tahoma 10"),
).pack(side = TOP,pady=5)

tkinter.Label(
    main,
    text="=> Red color -> Incompleted Task",
    background="#1d1d1d",
    width=50,
    foreground="red",
    font=("tahoma 10"),
).pack(side = TOP,pady=5)

tkinter.Label(
    main,
    text="=> orange color -> Next Task",
    background="#1d1d1d",
    width=50,
    foreground="orange",
    font=("tahoma 10"),
).pack(side = TOP,pady=5)

tkinter.Label(
    main,
    text="=> Green color -> completed Task",
    background="#1d1d1d",
    foreground="green",
    width=50,
    font=("tahoma 10"),
).pack(side = TOP)

tkinter.Label(
    main,
    text="=> Yellow color -> Failed Task",
    background="#1d1d1d",
    width=50,
    foreground="yellow",
    font=("tahoma 10"),
).pack(side = TOP,pady=5)



main.mainloop()

