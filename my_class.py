from tkinter import *
from datetime import datetime
from database import cursor,connection
from configparser import ConfigParser

#obtain the date and time


#window=Tk()
class AdmissionList:
    '''creates row on the admission page to add patient details, since am using grid, i need to 
    know the grid to pop the next row, to solve this i pass the column and row number i want when 
    calling the class in main as 'a' and 'b', which i used to determine which row and column to be in.
    '''
    def __init__(self,a,b,window=None,):
       
        self.window=window
        self.a=a
        self.b=b
        self.create_line()
        self.config=ConfigParser()
        
    def admit(self):
        '''admits the patient, adds to the database, and disables all entries'''
        self.connection=connection
        self.cursor=cursor
        self.get_info()
        self.date.config(state='disabled')
        self.bed.config(state='disabled')
        self.name.config(state='disabled')
        self.age.config(state='disabled')
        self.birth.config(state='disabled')
        self.gender.config(state='disabled')
        self.hosp.config(state='disabled')
        self.admit_button.config(state='disabled')
        self.discharge_button.config(state='normal')
        self.goto_button.config(state='normal')
        #add to database
        #col="CREATE TABLE details(Name VARCHAR(55),Age VARCHAR(20),Birth VARCHAR(20),Gender VARCHAR(20),HospNo VARCHAR(50),Admdate VARCHAR(20))"
        #self.cursor.execute(col)
        query="INSERT INTO details VALUES(%s,%s,%s,%s,%s,%s)"
        values=(name,age,birth,gender,hosp,adm_date)
        self.cursor.execute(query,values)
        self.connection.commit()
        
        #creates the config file
        self.createNewconfig()
        
    def discharge(self):
        '''first enables all entries, and clears the box, removes pt from the main database and 
        adds to the discharged list'''
        self.bed.config(state='normal')
        self.name.config(state='normal')
        self.age.config(state='normal')
        self.birth.config(state='normal')
        self.gender.config(state='normal')
        self.hosp.config(state='normal')
        self.date.config(state='normal')
        
        self.date.delete(0,END)
        self.bed.delete(0,END)
        self.name.delete(0,END)
        self.birth.delete(0,END)
        self.age.delete(0,END)
        self.gender.delete(0,END)
        self.hosp.delete(0,END)
        
        self.admit_button.config(state='normal')
        self.discharge_button.config(state='disabled')
        self.goto_button.config(state='disabled')
        
    def create_line(self):
        '''creates the rows to input patient data, and admit button.'''
        self.date=Entry(self.window,font=('ariel',12))
        self.date.grid(column=self.a, row=self.b)
        global date
        date=datetime.now().strftime("%Y-%m-%d %H:%M")
        self.date.insert(0,date)
        
  
        
        self.bed=Entry(self.window,font=('ariel',12),width=5)
        self.bed.grid(column=self.a+1, row=self.b)
    
    
    
        self.name=Entry(self.window,font=('ariel',12))
        self.name.grid(column=self.a+2, row=self.b)
    
        self.birth=Entry(self.window,font=('ariel',12),width=10)
        self.birth.grid(column=self.a+3,row=self.b)
        
        self.age=Entry(self.window,font=('ariel',12), width=5)
        self.age.grid(column=self.a+4, row=self.b)
    
        self.gender=Entry(self.window,font=('ariel',12),width=10)
        self.gender.grid(column=self.a+5, row=self.b)
    
        self.hosp=Entry(self.window,font=('ariel',12),width=12)
        self.hosp.grid(column=self.a+6, row=self.b)
        
        
        #buttons
        self.admit_button=Button(self.window,text='Admit',padx=10,font=('ariel',12),command=self.admit)
        self.admit_button.grid(column=self.a+7,row=self.b)
        
        self.goto_button=Button(self.window,text='Go To',font=('ariel',12),padx=10,state='disabled',command=self.goto)
        self.goto_button.grid(column=self.a+8,row=self.b)
        
        self.discharge_button=Button(self.window,text='Discharge',state='disabled',font=('ariel',12),padx=10,command=self.discharge)
        self.discharge_button.grid(column=self.a+9,row=self.b)
        
        
        
    def get_info(self):
        '''collects the details entered to be used later'''
        global bed,name,age,hosp,adm_date,birth,gender
        
        bed=self.bed.get()
        name=self.name.get()
        age=self.age.get()
        gender=self.gender.get()
        birth=self.birth.get()
        hosp=self.hosp.get()
        adm_date=self.date.get()
        
        
    def createNewconfig(self):
        '''creates the config file, sets the initial parameters'''   
       #creates an instance of the config parser, reads the parser file
        
        
        self.config.read('config.ini')
        #checks to see if the hospital number is in the config sections.
        #if not it writes a new section with the hosp number, and writes a key of starttime and sets it to an empty string.
        #added represents the num of time the add chart button was clicked 
        if hosp not in self.config.sections():
            self.config[hosp]={}
            #creates a starttime for obs and how many are added overall.
            self.config[hosp]['obs_starttime']=''
            self.config[hosp]['obs_count']='13'
            
            self.config[hosp]['nur_note_starttime']=''
            self.config[hosp]['nur_notes_count']='1'
            
            self.config[hosp]['med_note_starttime']=''
            self.config[hosp]['med_notes_count']='1'
            
            with open ('config.ini','w') as configfile:
                self.config.write(configfile)
            
        
        
        
    
    def goto(self):
        '''opens the patients chart.'''
        
        import outline_class
# n=0
# def add_chart():
    
#     global n
#     n=n+100
#     print (n)
  



                
                
                        
        
                