from tkinter import *
from tkinter import messagebox
from my_class import AdmissionList
window=Tk()
window.minsize(500,500)

window.title('Patient List')

window.config(padx=20,pady=20)


n=0

def add_row():
    '''creates an instance of the admissionlist class with grid parameters which
   increases the row value by 1 everytime it is called.
    '''
    global n
    
    
    n+=1
    admission_line=AdmissionList(0,n+2)
    
label_admission=Label(window,text='Admitted Patients',pady=10,font=('ariel',14)).grid(column=0,row=0,columnspan=4)

#buttons
admission_button=Button(window,text='New Admission',pady=5,padx=5,font=('ariel',10),command=add_row).grid(column=0,row=1) #runs the function check
find_patient=Button(window,text='Find Patient',padx=5,pady=5,font=('ariel',10)).grid(column=1,row=1)

#label for headings

Label(window,text='Admission Date',padx=10,pady=10,font=('ariel',12)).grid(column=0, row=2)
Label(window,text='Bed No',padx=10,pady=10,font=('ariel',12)).grid(column=1, row=2)
Label(window,text='Patient Name',padx=10,pady=10,font=('ariel',12)).grid(column=2, row=2)
Label(window,text='Date of Birth',padx=10,pady=10,font=('ariel',12)).grid(column=3, row=2)
Label(window,text='Age',padx=10,pady=10,font=('ariel',12)).grid(column=4, row=2)
Label(window,text='Gender',padx=10,pady=10,font=('ariel',12)).grid(column=5, row=2)
Label(window,text='Hosp No',padx=10,pady=10,font=('ariel',12)).grid(column=6, row=2)


        
        
           
window.mainloop()       