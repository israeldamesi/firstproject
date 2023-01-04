from tkinter import *
from tkinter import Frame

window=Tk()
window.title('Intellispace Login Page')
window.geometry('350x350')
window.config(bg='light blue',padx=20,pady=10)

heading_frame=Frame(window,bg='blue')
heading_frame.grid(column=0,row=0,columnspan=2,padx=5,pady=15)

login_label=Label(heading_frame,text='Login Page',font=('ariel',16),bg='light blue')
login_label.grid(column=1,row=0,padx=0,pady=5)

body_frame=Frame(window,padx=30)
body_frame.grid(row=1, column=0, columnspan=2)

username_label=Label(body_frame,text='Username',font=('ariel',12),padx=20,pady=10)
username_label.grid(row=2,column=0)

password_label=Label(body_frame,text='Password',font=('ariel',12),padx=20,pady=10)
password_label.grid(row=3, column=0)

username_entry=Entry(body_frame).grid(row=2,column=2)
password_entry=Entry(body_frame).grid(row=3,column=2)

def submit():
    window.destroy()
    from main import AdmissionList
def cancel():
    window.quit()
submit_button=Button(text='Submit',command=submit,pady=5).grid(column=1,row=4)
cancel_button=Button(text='Cancel',command=cancel,pady=5).grid(column=2,row=4)





window.mainloop()