from tkinter import *
from tkinter import messagebox  #for alert messages
from datetime import datetime,timedelta
from tkinter import ttk #for combobox
#from chart import PatientChart
#timedelta allows to increase time and date to a future date.




#import from database.py
from database import cursor,connection


class PatientChart:
    '''creates the patient's page, with obs, med and nursing notes'''
    def __init__(self,hosp,window=None):
        
        self.run=window
        self.run.geometry('1500x1000')
        self.run.title("One Community Hospital: Patient's Details")
        self.run.config(padx=30,pady=30,bg='white')
        self.hosp=hosp
        #self.run.grab_set() #allows to lock or attach a parent window to the child
        self.create_frame()
        self.side_pane()
        self.top_pane()
        
       #initial x-axis of obs entries
        self.x=25
        #the value to increase the size of the obs frame by everytime the button is clicked.
        self.inc=65
        #nursing and medical note frame, initial y axis 
        #self.note_n_frame_y=10
        #self.note_m_frame_y=10
        
        #the number of times the obs button is clicked
        self.n=0
        
        
        self.n_note_num=0
        
       
        
        
        #add icon to the title page
        self.image=PhotoImage(file='cardiogram.png')
        self.run.iconphoto(False,self.image)
        
        #call the patient detail page once the instance of the patientchart is created
        self.patient_page()
        
        
    def create_frame(self):
        '''creates  mainframe, side_frame and topframe on the page'''
        
        #creates the top frame
        self.top_frame=Frame(self.run,background="#A3DCF8")
        self.top_frame.place(x=0,y=20,width=1400,height=50)
       
    
        
    
        #creates the main frame
        
        self.main_frame=Frame(self.run,background='#f3f3f3',padx=20,pady=30)
        self.main_frame.place(x=170,y=130,width=1240,height=600)
        #self.main_frame.pack_propagate(True)
        
        
       ##creates side frame
        self.side_frame=Frame(self.run,background='white',pady=30)
        self.side_frame.place(x=0,y=130,width=130,height=600)
        #self.side_frame.pack_propagate(False)  ##allow you to set your own width and height
        
       
    def patient_page(self):
        '''creates the patient details page, when you click the goto button
        connects to the database to collect admission info'''
   
            #main frame
            
        self.clear_frame()  ##clear old frame
        
        self.unselect_buttons()
        
        self.selected_button(self.details_button)
        Label(self.main_frame,text='Patient Details' ,font=('ariel',14),anchor=W).place(x=25,y=25)
        Label(self.main_frame,text='Patient Name' ,font=('ariel',12),width=20,anchor=W).place(x=25,y=75)
        Label(self.main_frame,text='Age' ,font=('ariel',12),width=20,anchor=W).place(x=25,y=125)
        Label(self.main_frame,text='Date of Birth',font=('ariel',12),width=20,anchor=W).place(x=25,y=175)
        Label(self.main_frame,text='Gender',font=('ariel',12),width=20,anchor=W).place(x=25,y=225)
        Label(self.main_frame,text='Date of Admission',font=('ariel',12),width=20,anchor=W).place(x=25,y=275)
        Label(self.main_frame,text='Hospital Number',font=('ariel',12),width=20,anchor=W).place(x=25,y=325)
        Label(self.main_frame,text='Next of Kin',font=('ariel',12),width=20,anchor=W).place(x=25,y=375)

        
        connection.reconnect()  
        sql="select * from admissions where hosp=%s"
        value=(hosp,)  ##this replaces the %s
        cursor.execute(sql,value)
        patient_info=cursor.fetchall()
        print(patient_info)
        
        entry_name=Entry(self.main_frame,font=('ariel',12))
        entry_name.place(x=250,y=75)
        entry_name.insert(0,patient_info[0][2])
        entry_name.config(state='disabled')

        entry_age=Entry(self.main_frame,font=('ariel',12))
        entry_age.place(x=250,y=125)
        entry_age.insert(0,patient_info[0][4])
        entry_age.config(state='disabled')

        entry_gender=Entry(self.main_frame,font=('ariel',12))
        entry_gender.place(x=250,y=175)
        
        entry_gender.insert(0,patient_info[0][5])
        entry_gender.config(state='disabled')
        
        entry_birth=Entry(self.main_frame,font=('ariel',12))
        entry_birth.place(x=250,y=225)
        entry_birth.insert(0,patient_info[0][3])
        entry_birth.config(state='disabled')
        
        entry_admission=Entry(self.main_frame,font=('ariel',12))
        entry_admission.place(x=250,y=275)
        entry_admission.insert(0,patient_info[0][0])
        entry_admission.config(state='disabled')

        entry_hosp=Entry(self.main_frame,font=('ariel',12))
        entry_hosp.place(x=250,y=325)
        entry_hosp.insert(0,patient_info[0][6])
        entry_hosp.config(state='disabled')

        entry_next=Entry(self.main_frame,font=('ariel',12))
        entry_next.place(x=250,y=375)
    
#occupies side frame
    def side_pane(self):
        '''creates the side pane, containing buttons'''
        
        ##buttons
        self.details_button=Button(self.side_frame,text='Patient Details',justify='left',font=('ariel',14),command=self.patient_page,pady=20,width=25,anchor=W)
        self.details_button.pack()
         
        self.obs_button=Button(self.side_frame,text='Observations',justify='left',font=('ariel',14),pady=20,width=25,anchor=W,command=self.obs_chart)
        self.obs_button.pack()

        self.nursing_notes_button=Button(self.side_frame,text='Nursing Notes',justify='left',font=('ariel',14),pady=20,width=25,anchor=W,command=self.create_nursing_frame)
        self.nursing_notes_button.pack()

        self.medical_notes_button=Button(self.side_frame,text='Medical Notes',justify='left',font=('ariel',14),pady=20,width=25,anchor=W,command=self.create_medical_frame)
        self.medical_notes_button.pack()
        
        self.drugs_button=Button(self.side_frame,text='Drugs',justify='left',font=('ariel',14),pady=20,width=25,command=self.drugs,anchor=W)
        self.drugs_button.pack()
        
    def selected_button(self,button):
        '''creates decoration for the selected button'''
        button.config(bd=0,bg='white')
        
    def unselect_buttons(self):
        '''set decorations for all buttons'''
        self.details_button.config(bd=2,bg='#81C6E8')
        self.obs_button.config(bd=2,bg='#81C6E8')
        self.nursing_notes_button.config(bd=2,bg='#81C6E8')
        self.medical_notes_button.config(bd=2,bg='#81C6E8')
        self.drugs_button.config(bd=2,bg='#81C6E8')
        
#top frame
    def top_pane(self):
        '''creates the top pane, connects to the database to collect info'''
        connection.reconnect()
        sql="select * from admissions where hosp=%s"
        value=(hosp,)
        cursor.execute(sql,value)
        details=cursor.fetchall()
       #creates labels, and collects data from database
        Label(self.top_frame,text='Bed No: '+str(details[0][1]),font=('ariel',12),bg="#A3DCF8").pack(side='left')
        Label(self.top_frame,text='\tPatient Name: '+details[0][2],font=('ariel',12),bg="#A3DCF8").pack(side='left')
        Label(self.top_frame,text='\tAge:' + str(details[0][4]),justify='left',font=('ariel',12),bg="#A3DCF8").pack(side='left')
        Label(self.top_frame,text='\tGender: ' + details[0][5],font=('ariel',12),bg="#A3DCF8").pack(side='left')
        Label(self.top_frame,text='\tDate of Birth: '+ str(details[0][3]),font=('ariel',12),bg="#A3DCF8").pack(side='left')
        Label(self.top_frame,text='\tHospital Number: ' + details[0][6],font=('ariel',12),bg="#A3DCF8").pack(side='left')
    
        
    def obs_chart(self):
        '''creates obs chart in the main frame when the obs button is clicked'''
        self.clear_frame()
        self.unselect_buttons()
        self.selected_button(self.obs_button)
        self.obs_button.config(bd=0)
        
        Label(self.main_frame,text='24 HOURS  OBSERVATION',font=('ariel',12,'bold')).place(x=400,y=2)
        
        Label(self.main_frame,text='Heart Rate',font=('ariel',12)).place(x=10,y=93)
        Label(self.main_frame,text='Blood Pressure',font=('ariel',12,)).place(x=10,y=130)
        Label(self.main_frame,text='Saturation',font=('ariel',12)).place(x=10,y=170)
        Label(self.main_frame,text='Temperature',font=('ariel',12)).place(x=10,y=210)
        Label(self.main_frame,text='Respiration',font=('ariel',12)).place(x=10,y=250)
        Label(self.main_frame,text='Pupil Size',font=('ariel',12)).place(x=10,y=290)
        Label(self.main_frame,text='Reaction',font=('ariel',12)).place(x=10,y=330)
        #when we creates the obs frame we want the col to start from 1
        self.col=1
        self.create_obs_frame()
        
        self.repopulate_obs()
        
        ##after repopulation save the final value of self.x (which is the x-axis) as x, then pass it to the create col fnx
        #so it can use it as the starting x-axis .
        global x
        x=self.x
        
        
        #create entries
    def create_obs_frame(self):
        '''creates a canvas and creates an obs frame in it '''
        #represents the initial value of x-axis
        self.x=20
        #creates a canvas which allows to scroll the frame.
        self.obs_canvas=Canvas(self.main_frame,height=500,width=1000)
        self.h=Scrollbar(self.run,orient=HORIZONTAL,command=self.obs_canvas.xview,)## creates a scrollbar in the main window (self.run)
        self.h.pack(side=BOTTOM,fill='x')
        self.obs_canvas.config(xscrollcommand=self.h.set)
        
        self.obs_canvas.place(x=130,y=50)
        
        #pops the obs_frame inside the obs_canvas, so we can scroll the frame
        self.obs_frame=Frame(self.obs_canvas,bg='#f3f3f3',width=1000,height=500, highlightbackground='black')
       
        self.obs_canvas.create_window((500,250),anchor=CENTER,window=self.obs_frame)
        
        
        
        #creates a button to add new obs
        self.add_obs=Button(self.main_frame,text='Add Chart',font=('ariel',12),command=self.add_entries,bg="#A3DCF8")
        self.add_obs.place(x=700,y=2)
        
        #creates button to save obs.
        self.save_obs=Button(self.main_frame,text='Save Chart',font=('ariel',12),command=self.save_entries,bg='#A3DCF8')
        self.save_obs.place(x=20,y=2)
      
    def create_col(self):
        '''creates a column of obs entries'''
        
        self.time=Label(self.obs_frame,font=('ariel',11),width=5)
        self.time.place(x=self.x,y=6)
       
        
        self.heartRate_entry=Entry(self.obs_frame,width=7,font=('ariel',11))
        self.heartRate_entry.place(x=self.x,y=48)
        
        self.bp_entry=Entry(self.obs_frame,width=7,font=('ariel',11)) 
        self.bp_entry.place(x=self.x,y=83)
        
        self.spo2_entry=Entry(self.obs_frame,width=7,font=('ariel',11)) 
        self.spo2_entry.place(x=self.x,y=123)
        
        self.temp_entry=Entry(self.obs_frame,width=7,font=('ariel',11)) 
        self.temp_entry.place(x=self.x,y=163)
        
        self.resp_entry=Entry(self.obs_frame,width=7,font=('ariel',11)) 
        self.resp_entry.place(x=self.x,y=203)
        
        self.pup_entry=Entry(self.obs_frame,width=7,font=('ariel',11)) 
        self.pup_entry.place(x=self.x,y=243)
        
        self.reaction_entry=Entry(self.obs_frame,width=7,font=('ariel',11)) 
        self.reaction_entry.place(x=self.x,y=283)
        
        
        #combobox
        #self.reaction_entry=ttk.Combobox(self.obs_frame,width=7)
        #self.reaction_entry['values']=('Normal','Brisk','Sluggish')
        #self.reaction_entry.place(x=self.x,y=283)
        #self.reaction_entry.pack(side=LEFT)

       
        #when i call populate else where it resets the value of self.x, solution is to get the self.x value from the repopulate funx
        #and use it here.
        global x
        if self.col==1:
            x=self.x ##this x value is sent to the repopulate fux, and used as the starting value of the x-axis
        self.x=x ##get the value of x(x-axis value) from repopulate after population, to be used as the x-axis here
        self.x+=65 ##increases the self.x value very time the function is called
        #column to go up by one everytime we create col
        self.col+=1
        
     
        
    def add_entries(self):    
        '''creates entries for observations. obtains the size of the frame and increases it by 75, each time the button is clicked
        this creates a new instance of the self.populate(), and hence resets the self.x value.'''
        
         #to accomodate new entries we have to increase the width of obs frame the width of each obs box.
        cur_time=datetime.now().strftime('%H:%M')

        same_day=datetime.today().strftime('%x')

        new_day=datetime.today()+timedelta(days=1)
        new_day=new_day.strftime('%x \n%H:%M')
        global x
        x=self.x
         
        self.create_col()
        
        
        
        #am using 2 because by the time the function by the it gets to this function the value of self.col
        if self.col==2:
            self.time.config(text=same_day +'\n' +cur_time,width=6,height=2)
        else:
            self.time.config(text=cur_time,width=6,height=2)
        if cur_time=='00:00':
            self.time.config(text=new_day)
            
        #starts to increase the size of the obs frame, when the number of cols is >16
        if self.col>=16:
            self.obs_frame.config(width=self.obs_frame.winfo_width()+self.inc)
        
        #give ability to scroll
        self.obs_canvas.config(scrollregion=self.obs_canvas.bbox('all'))
        
    def get_obs_values(self):
        '''obtains the values of data entered into obs entries'''
        global time,heartrate,bp,spo2,temp,resp,pup,reaction
        #time is a label use cget() to obtain text
        
        time=self.time.cget('text')
        heartrate=self.heartRate_entry.get()
        bp=self.bp_entry.get()
        spo2=self.spo2_entry.get()
        temp=self.temp_entry.get()
        resp=self.resp_entry.get()
        pup=self.pup_entry.get()
        reaction=self.reaction_entry.get()
        
        #hosp the hospital number is already global from self.go_to 
        
    def disable_obs_entries(self):
        """Disabled entries after saving"""
        self.heartRate_entry.config(state='disabled')
        self.spo2_entry.config(state='disabled')
        self.bp_entry.config(state='disabled')
        self.temp_entry.config(state='disabled')
        self.resp_entry.config(state='disabled')
        self.pup_entry.config(state='disabled')
        self.reaction_entry.config(state='disabled')
         
    def save_entries(self):
        '''saves obs into the database, using data from get_obs_values()'''
        self.get_obs_values()
        try:
            sql="INSERT INTO OBS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values=(time,heartrate,bp,spo2,temp,resp,pup,reaction,hosp)
            cursor.execute(sql,values)
            connection.commit()
            connection.close()
            self.disable_obs_entries()
        except:
            messagebox.showerror(title='Error',message='Ensure the right values are entered')
            
        
    def repopulate_obs(self):
        """connects to the database, and repopulates the obs_frame with the data"""
        connection.reconnect()
        sql="select * from obs where hosp=%s"
        value=(hosp,)
        cursor.execute(sql,value)
        obs=cursor.fetchall()
        #creates a for loop, calls the create_col() each time, filling it with data, disabling them after
        for ob in obs:
            self.create_col()
            self.time.config(text=ob[0])
            
            self.heartRate_entry.insert(0,ob[1])
            self.heartRate_entry.config(state='disabled')
            
            self.bp_entry.insert(0,ob[2])
            self.bp_entry.config(state='disabled')
            self.spo2_entry.insert(0,ob[3])
            self.spo2_entry.config(state='disabled')
            self.temp_entry.insert(0,ob[4])
            self.temp_entry.config(state='disabled')
            self.resp_entry.insert(0,ob[5])
            self.resp_entry.config(state='disabled')
            self.pup_entry.insert(0,ob[6])
            self.pup_entry.config(state='disabled')
            self.reaction_entry.insert(0,ob[7])
            self.reaction_entry.config(state='disabled')
            
       
    def clear_frame(self):
        '''you have to clear the frame of all widget to be to pop new widgets inside.'''
        for frame in self.main_frame.winfo_children():
            frame.destroy()
       
    def create_nursing_frame(self):
        '''creates the nursing frame, with buttons'''
        
        self.clear_frame()
        self.unselect_buttons()
        self.selected_button(self.nursing_notes_button)
        self.note_n_frame_y=10
        Label(self.main_frame,text='Nursing Notes',font=('verdana',15,'bold')).place(x=300,y=2)
       
        self.canvas=Canvas(self.main_frame,width=1200, height=500)
        self.canvas.place(x=5,y=50)
        self.nursing_frame=Frame(self.canvas,width=1200,height=500,bg='#f3f3f3')
        
        self.canvas.create_window((600,250),anchor=CENTER,window=self.nursing_frame)
        
        self.scroll=Scrollbar(self.main_frame,orient='vertical',command=self.canvas.yview)
        self.scroll.pack(side='right',fill=Y)
        self.canvas.config(yscrollcommand=self.scroll.set)
        
        self.save_nursing_note=Button(self.main_frame,text='Save Note',font=('ariel',12),bg="#A3DCF8",command=self.save_nursing_note)
        self.save_nursing_note.place(x=20,y=2)
        self.add_nursing_note=Button(self.main_frame,text='Add Note',font=('ariel',12),bg="#A3DCF8",command=self.new_nursing_note)
        self.add_nursing_note.place(x=500,y=2)
        self.readOldDate_nursing()
        self.writeOldDate_nursing()
        
        #reset the self.note_n_frame_y value, to that the frame can start from the original y value, when you re-click, otherwise it starts from
        #the increase y value.
    
    def readOldDate_nursing(self):
        '''creates a connection to the database'''
        connection.reconnect()
        sql="select * from nursingnote where hosp=%s"
        value=(hosp,)
        cursor.execute(sql,value)
        global note_data
        note_data=cursor.fetchall()
        return note_data 
    
    def writeOldDate_nursing(self):
        '''creates nursing note and writes old data to note'''
        for note  in self.readOldDate_nursing():
            self.new_nursing_note()
            self.nur_dateLabel.config(text=note[1])
            self.nurse_name.insert(0,note[2])
            self.nurse_name.config(state='disabled')
            self.nurse_note.insert(END,note[3])
            self.nurse_note.config(state=DISABLED)   
        
    def new_nursing_note(self):
        '''Add nursing note when the button is clicked.'''
       
        
        self.today=datetime.now().strftime('%D %H:%M')
        self.note_frame=Frame(self.nursing_frame,bg='#f3f3f3',width=900,height=500)
        self.note_frame.place(x=15,y=self.note_n_frame_y)
        
        Label(self.note_frame,text='Date and Time',font=('verdana',12)).place(x=5,y=50)
        self.nur_dateLabel=Label(self.note_frame,text=self.today,font=('verdana',12))
        self.nur_dateLabel.place(x=180,y=50)
        Label(self.note_frame,text='Name of Nurse',font=('verdana',12)).place(x=5,y=85)
        
        
        
        self.nurse_name=Entry(self.note_frame,font=('verdana',12))
        self.nurse_name.place(x=180,y=85)
        Label(self.note_frame,text='Notes',font=('verdana',12)).place(x=5,y=200)
        self.nurse_note=Text(self.note_frame,width=50,height=15,font=('verdana',12))
        self.nurse_note.place(x=180,y=120)
        
        self.note_n_frame_y+=500     
        
        self.nursing_frame.config(height=self.nursing_frame.winfo_height()+500)
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        
        
        
    
    
    def writeDatabase_nursing(self):
        connection.reconnect()
        write="insert into nursingNote values(%s,%s,%s,%s)"
        #data from the nurse note entries
        values=(hosp,self.today,self.nurse_name.get(),self.nurse_note.get('1.0',END))
        cursor.execute(write,values)
        connection.commit()
        connection.close()
        
        
    
    def save_nursing_note(self):
        
        self.writeDatabase_nursing()
        
        self.disable_entries('nur') 
            
        
    
    def disable_entries(self,data):
        
        if data== 'med':
            self.doc_name.config(state='disabled')
            self.med_note.config(state='disabled')
        if data =='nur':
            self.nurse_name.config(state='disabled')
            self.nurse_note.config(state=DISABLED)
            
    def save_medical_note(self):
        
        self.writeDatabase_medical()
       
        self.disable_entries('med')
                 
        
    def create_medical_frame(self):
        self.clear_frame()
        self.unselect_buttons()
        self.selected_button(self.medical_notes_button)
        self.note_m_frame_y=10
        Label(self.main_frame,text='Medical Notes',font=('verdana',15,'bold')).place(x=300,y=2)
        self.add_medical_note=Button(self.main_frame,text='Add Note',font=('ariel',12),bg="#A3DCF8",command=self.new_medical_note)
        self.add_medical_note.place(x=500,y=2)
        
        self.save_medical_note=Button(self.main_frame,text='Save Note',font=('ariel',12),bg="#A3DCF8",command=self.save_medical_note)
        self.save_medical_note.place(x=10,y=2)
        
        self.canvas=Canvas(self.main_frame,width=1200, height=500)
        self.canvas.place(x=5,y=50)
        self.medical_frame=Frame(self.canvas,width=1200,height=500,bg='#f3f3f3')
        
        self.canvas.create_window((600,250),anchor=CENTER,window=self.medical_frame)
        
        self.scroll=Scrollbar(self.main_frame,orient='vertical',command=self.canvas.yview)
        self.scroll.pack(side='right',fill=Y)
        self.canvas.config(yscrollcommand=self.scroll.set)
        
        self.readOldDate_medical()
        self.writeOldDate_medical()
        #reset the self.note_n_frame_y value, to that the frame can start from the original y value, when you re-click, otherwise it starts from
        #the increase y value.
     
    def writeDatabase_medical(self):
        print(self.doc_name.get(),self.med_note.get('1.0',END))
        '''writes data to the medicalNote database'''
        connection.reconnect()
        write="insert into medicalNote values(%s,%s,%s,%s)"
        #data from the nurse note entries
        values=(hosp,self.today,self.doc_name.get(),self.med_note.get('1.0',END))
        cursor.execute(write,values)
        connection.commit()
        connection.close()
        
    def readOldDate_medical(self):
        '''creates a connection to the database'''
        connection.reconnect()
        sql="select * from medicalnote where hosp=%s"
        value=(hosp,)
        cursor.execute(sql,value)
        global note_data
        note_data=cursor.fetchall()
        return note_data 
    
    def writeOldDate_medical(self):
        '''creates nursing note and writes old data to note'''
        for note  in self.readOldDate_medical():
            self.new_medical_note()
            self.med_dateLabel.config(text=note[1])
            
            self.doc_name.insert(0,note[2])
            self.doc_name.config(state='disabled')
            self.med_note.insert(END,note[3])
            self.med_note.config(state='disabled')
            connection.close()       
        
        
     
        
    def new_medical_note(self):
        '''Adds medical note when the button is clicked'''
        
        self.today=datetime.now().strftime('%D %H:%M')
        
        self.note_frame=Frame(self.medical_frame,bg='#f3f3f3',width=900,height=500)
        self.note_frame.place(x=10,y=self.note_m_frame_y)
        Label(self.note_frame,text='Date and Time',font=('verdana',12)).place(x=5,y=50)
        
        self.med_dateLabel=Label(self.note_frame,text=self.today,font=('verdana',12))
        self.med_dateLabel.place(x=180,y=50)
        
        Label(self.note_frame,text='Name of Nurse',font=('verdana',12)).place(x=5,y=85)
        
        self.doc_name=Entry(self.note_frame,font=('verdana',12))
        self.doc_name.place(x=180,y=85)
        Label(self.note_frame,text='Notes',font=('verdana',12)).place(x=5,y=200)
        self.med_note=Text(self.note_frame,width=50,height=15,font=('verdana',12))
        self.med_note.place(x=180,y=120)
        
        self.note_m_frame_y+=500
        #self.nursing_frame_height+=300
        self.medical_frame.config(height=self.medical_frame.winfo_height()+500)
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        
        
   
    def drugs(self):
        self.clear_frame()
        self.unselect_buttons()
        self.selected_button(self.drugs_button)
        
        print(self.x)
#n represents the row number to start creating the admission list from
start_row=4

class CreateRow(PatientChart):
    """To make each row related to the buttons you need a class to create these rows."""
    def __init__(self,window=None):
       
       
        global start_row
        self.window=window
        
        
        self.create_line(a=0,b=start_row)
        start_row+=1
    
    
    def create_line(self,a,b):
        '''creates the rows to input patient data, and admit button.'''
        self.a=a
        self.b=b
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
        self.birth.insert(0,'YYYY-MM-DD')
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
        
    def admit(self):
        '''admits the patient, adds to the database, and disables all entries'''
        
        
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
        
        self.writedata_database()
        
    def writedata_database(self):
        connection.reconnect()
        self.get_info()
        try:
            sql= "insert into Admissions values(%s,%s,%s,%s,%s,%s,%s)"
            values=(adm_date_info,bed_info,name_info,birth_info,age_info,gender_info,hosp_info)
            cursor.execute(sql,values)
            connection.commit()
            connection.close()
        except:
            
            messagebox.showerror(title='ValueError',message='Ensure Bed is a unique number, hospital number is unique and Date of Birth in right format')
            self.discharge()
            self.date.insert(0,date)
            self.birth.insert(0,'YYYY-MM-DD')
            
            

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
    
    def get_info(self):
        '''collects the details entered to be used later'''
        global bed_info,name_info,age_info,gender_info,birth_info,adm_date_info,hosp_info
        bed_info=self.bed.get()
        name_info=self.name.get()
        age_info=self.age.get()
        gender_info=self.gender.get()
        birth_info=self.birth.get()
        adm_date_info=self.date.get()
        hosp_info=self.hosp.get()
        
        
    def goto(self):
        '''opens the patients chart.'''
        self.hosp.config(state='normal')
        
        #this allows me to grab a hosp of the hospital number anywhere in the file
        global hosp
        hosp=self.hosp.get()
        self.hosp.config(state='disabled')
        chart=PatientChart(hosp,window=Toplevel())
        
       



class Main(CreateRow):
    
    def __init__(self,window=Tk()):
        
        #
        #super().__init__()
        self.window=window
        self.window.minsize(500,500)
       
        self.window.title('One Community Hospital: Admission List')

        self.window.config(padx=20,pady=20)
        self.n=3
        self.create_labels()
        self.populate_admissionfields()
        
        self.image=PhotoImage(file='cardiogram.png')
        self.window.iconphoto(False,self.image)
        
        self.window.mainloop() 
   
    
    def readdata_database(self):
        connection.reconnect()
       
        sql="select * from Admissions"
       
        cursor.execute(sql)
        self.adm_list=cursor.fetchall()
        print(self.adm_list)
        return self.adm_list

    def populate_admissionfields(self):
        #self.a=CreateRow()
        
        for patient_details in self.readdata_database():
            #self.line represent the an instance of the createrow class, the super()__init__() gives me access 
            #to all the methods in the createrow call, but using in this class throws an error becuase the 
            #super class automatically calls the createrow class, which inturn creates a row, which i dont need, to solve
            #i removed the init class and called the class directly where i need it.but calling it each time on each attribute 
            #creates a row which i done need, so i saved it as self and used it.
            self.line=CreateRow()
            
            self.line.date.delete(0,END)
            self.line.date.insert(0,patient_details[0])
           
            self.line.date.config(state='disabled')
            
            self.line.date.delete(0,END)
            self.line.bed.insert(0,patient_details[1])
            self.line.bed.config(state='disabled')
            
            self.line.name.insert(0,patient_details[2])
            self.line.name.config(state='disabled')
            
            self.line.birth.insert(0,patient_details[3])
            self.line.birth.config(state='disabled')
            
            self.line.age.insert(0,patient_details[4])
            self.line.age.config(state='disabled')
            
            self.line.gender.insert(0,patient_details[5])
            self.line.gender.config(state='disabled')
            
            self.line.hosp.insert(0,patient_details[6])
            self.line.hosp.config(state='disabled')
            
            self.line.admit_button.config(state='disabled')
            self.line.goto_button.config(state='normal')
            self.line.discharge_button.config(state='normal')
            
            print(f' inserted {patient_details}')
        
    def add_row(self):
        '''when i click the admit button, it creates an instance of create_row class, and calls it with
        column and row values.
        '''
        global n
       
        create_row=CreateRow()
        
        
        
        
    def create_labels(self):
        label_admission=Label(self.window,text='Admitted Patients',pady=10,font=('ariel',14)).grid(column=0,row=0,columnspan=4)

        #buttons
        admission_button=Button(self.window,text='New Admission',pady=5,padx=5,font=('ariel',10),command=self.add_row).grid(column=0,row=1) #runs the function check
        find_patient=Button(self.window,text='Find Patient',padx=5,pady=5,font=('ariel',10)).grid(column=1,row=1)

        #label for headings

        Label(self.window,text='Admission Date',padx=10,pady=10,font=('ariel',12)).grid(column=0, row=2)
        Label(self.window,text='Bed No',padx=10,pady=10,font=('ariel',12)).grid(column=1, row=2)
        Label(self.window,text='Patient Name',padx=10,pady=10,font=('ariel',12)).grid(column=2, row=2)
        Label(self.window,text='Date of Birth',padx=10,pady=10,font=('ariel',12)).grid(column=3, row=2)
        Label(self.window,text='Age',padx=10,pady=10,font=('ariel',12)).grid(column=4, row=2)
        Label(self.window,text='Gender',padx=10,pady=10,font=('ariel',12)).grid(column=5, row=2)
        Label(self.window,text='Hosp No',padx=10,pady=10,font=('ariel',12)).grid(column=6, row=2)


        
    
        
main=Main()


