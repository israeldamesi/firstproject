from tkinter import *
from my_class import *
from datetime import datetime
from configparser import ConfigParser

#obtains the hr element from datetime

cur_hr=datetime.now().strftime('%H')
cur_hr+='00'
cur_hr=int(cur_hr)


        
#create instance of DateAndTime class




class PatientChart:
    '''creates the patient's page, with obs, med and nursing notes'''
    def __init__(self,run=Toplevel()):
        self.run=run
        self.run.geometry('1500x1000')
        self.run.title('Details')
        self.run.config(padx=30,pady=30)
        
        #self.run.grab_set()
        self.create_frame()
        self.side_pane()
        self.top_pane()
        self.hr=cur_hr
        # space between obs entrys
        self.x=25
        #initial vaules
        self.inc=75
        #nursing and medical note frame, initial y axis 
        self.note_n_frame_y=10
        self.note_m_frame_y=10
        #creates the config instance and reads the config file
        self.config=ConfigParser()
        self.config.read('config.ini')
        
        
        
        
    def create_frame(self):
        #creates top frame
        self.top_frame=Frame(self.run,background='green')
        self.top_frame.place(x=0,y=0,width=1400,height=50)
        #self.top_frame.pack_propagate(False)
        
        
        #top frame lower
        self.top_frame_lower=Frame(self.run,background='brown')
        self.top_frame_lower.place(x=0,y=50,width=1400,height=50)
        #self.top_frame_lower.place_propagate(False)
    
        
    
        #creates the main frame
        self.main_frame=Frame(self.run,background='red',padx=20,pady=30)
        self.main_frame.place(x=170,y=130,width=1240,height=600)
        #self.main_frame.pack_propagate(True)
        
        
       ##creates side frame
        self.side_frame=Frame(self.run,background='blue',pady=30)
        self.side_frame.place(x=0,y=130,width=130,height=600)
        #self.side_frame.pack_propagate(False)  ##allow you to set your own width and height
        
        
        
        
    def patient_page(self):
   
            #main frame
        self.clear_frame()
        Label(self.main_frame,text='Patient Details' ,font=('ariel',14),anchor=W).place(x=25,y=25)
        Label(self.main_frame,text='Patient Name' ,font=('ariel',12),width=20,anchor=W).place(x=25,y=75)
        Label(self.main_frame,text='Age' ,font=('ariel',12),width=20,anchor=W).place(x=25,y=125)
        Label(self.main_frame,text='Date of Birth',font=('ariel',12),width=20,anchor=W).place(x=25,y=175)
        Label(self.main_frame,text='Gender',font=('ariel',12),width=20,anchor=W).place(x=25,y=225)
        Label(self.main_frame,text='Date of Admission',font=('ariel',12),width=20,anchor=W).place(x=25,y=275)
        Label(self.main_frame,text='Hospital Number',font=('ariel',12),width=20,anchor=W).place(x=25,y=325)
        Label(self.main_frame,text='Next of Kin',font=('ariel',12),width=20,anchor=W).place(x=25,y=375)

        entry_name=Entry(self.main_frame,font=('ariel',12))
        entry_name.place(x=250,y=75)
        entry_name.insert(0,name)
        entry_name.config(state='disabled')

        entry_age=Entry(self.main_frame,font=('ariel',12))
        entry_age.place(x=250,y=125)
        entry_age.insert(0,age)
        entry_age.config(state='disabled')

        entry_gender=Entry(self.main_frame,font=('ariel',12))
        entry_gender.place(x=250,y=175)
        
        entry_gender.insert(0,gender)
        entry_gender.config(state='disabled')
        
        entry_birth=Entry(self.main_frame,font=('ariel',12))
        entry_birth.place(x=250,y=225)
        entry_birth.insert(0,birth)
        entry_birth.config(state='disabled')
        
        entry_admission=Entry(self.main_frame,font=('ariel',12))
        entry_admission.place(x=250,y=275)
        entry_admission.insert(0,adm_date)
        entry_admission.config(state='disabled')

        entry_hosp=Entry(self.main_frame,font=('ariel',12))
        entry_hosp.place(x=250,y=325)
        entry_hosp.insert(0,hosp)
        entry_hosp.config(state='disabled')

        entry_next=Entry(self.main_frame,font=('ariel',12))
        entry_next.place(x=250,y=375)
        
        
        


#occupies side frame
    def side_pane(self):
        
        
        self.details=Button(self.side_frame,text='Patient Details',justify='left',font=('ariel',14),command=self.patient_page,pady=20,width=25,anchor=W)
        self.details.pack()
         
        self.obs=Button(self.side_frame,text='Observations',justify='left',font=('ariel',14),pady=20,width=25,anchor=W,bd=0,command=self.obs_chart)
        self.obs.pack()

        self.nursing_notes=Button(self.side_frame,text='Nursing Notes',justify='left',font=('ariel',14),pady=20,width=25,anchor=W,command=self.create_nursing_frame)
        self.nursing_notes.pack()

        self.medical_notes=Button(self.side_frame,text='Medical Notes',justify='left',font=('ariel',14),pady=20,width=25,anchor=W,command=self.create_medical_frame)
        self.medical_notes.pack()
        self.drugs=Button(self.side_frame,text='Drugs',justify='left',font=('ariel',14),pady=20,width=25,command=self.drugs,anchor=W)
        self.drugs.pack()
#top frame
    def top_pane(self):
        
        add_doc=Button(self.top_frame,text='Add New\nDocument',font=('ariel',11))
        add_doc.place(x=0,y=0)
        save=Button(self.top_frame,text='Save Chart',font=('ariel',11))
        save.place(x=120,y=15)
        Label(self.top_frame_lower,text='Patient Name: '+ name,font=('ariel',12)).pack(side='left')
        Label(self.top_frame_lower,text='\tAge:' + age,justify='left',font=('ariel',12)).pack(side='left')
        Label(self.top_frame_lower,text='\tGender: ' + gender,font=('ariel',12)).pack(side='left')
        Label(self.top_frame_lower,text='\tDate of Birth: '+ birth,font=('ariel',12)).pack(side='left')
        Label(self.top_frame_lower,text='\tHospital Number: ' + hosp,font=('ariel',12)).pack(side='left')
    
    def obs_chart(self):
        '''creates obs chart in the main frame when the obs button is clicked'''
        self.clear_frame()
        Label(self.main_frame,text='24 HOURS  OBSERVATION',font=('ariel',12,'bold')).place(x=400,y=2)
        
        Label(self.main_frame,text='Heart Rate',font=('ariel',12)).place(x=10,y=90)
        Label(self.main_frame,text='Blood Pressure',font=('ariel',12,)).place(x=10,y=130)
        Label(self.main_frame,text='Saturation',font=('ariel',12)).place(x=10,y=170)
        Label(self.main_frame,text='Temperature',font=('ariel',12)).place(x=10,y=210)
        Label(self.main_frame,text='Respiration',font=('ariel',12)).place(x=10,y=250)
        Label(self.main_frame,text='Pupil Size',font=('ariel',12)).place(x=10,y=290)
        Label(self.main_frame,text='Reaction',font=('ariel',12)).place(x=10,y=330)
       
        self.create_obs_frame()
        self.readConfig_Starttime('obs_starttime')
        self.readConfig_populate('obs_count')
        
        
               
         #reset the value of self.x=25, everytime the create frame runs it increase the value of x i dont know why
        self.x=25
        
        
    def readConfig_Starttime(self,key):
        '''Reads the config file for the time the obs was started for the patient.
        key here is the start time of the chart from the config file'''
        # config=ConfigParser()
        # config.read('config.ini')
        self.key=key
        #check the value of starttime, if its '' then set it to self.hr, else use what is there as the self.hr
       
            
        
        if self.config[hosp][self.key]=='':
            self.config[hosp][self.key]=str(self.hr)
            
            with open('config.ini','w') as configfile:
                self.config.write(configfile) 
                    
        elif self.config[hosp][self.key]!='':
            self.config.read('config.ini')
            saved_time=self.config[hosp][self.key]
            self.hr=int(saved_time)
           
        
        
        #added represent the number of time a button was clicked to add obs chart, this is saved in the config file
        #we want the program to show all these after the first 13 obs,, so we retrieve that number from config.ini,
        # convert to int and use a loop to run add entries.
    def readConfig_populate(self,key):
        
        '''Reads the config file for changes when the program last run and populates the page 
        with those changes.need to call it with the count in config'''
        self.key=key
        
        
        self.config.read('config.ini')
        to_add=int(self.config[hosp][self.key])
        
            
        
        if self.key=='obs_count':
               
            self.add_old_entries()
                
            
                
        elif self.key=='nur_notes_count':
            
            for i in range(to_add):
                self.new_nursing_note()
                
                
        elif self.key=='med_notes_count':
            for i in range(to_add):
                self.new_medical_note()

         #reset the key to the initial value and write.
        self.config[hosp][self.key]=str(to_add)
        
        with open('config.ini','w')as configfile:
            self.config.write(configfile)
        
        
        
        #create entries
    def create_obs_frame(self):
        '''creates a canvas create an obs frame, '''
       
        self.obs_canvas=Canvas(self.main_frame,height=500,width=1000)
        self.h=Scrollbar(self.main_frame,orient=HORIZONTAL,command=self.obs_canvas.xview,)
        self.h.pack(side=BOTTOM,fill='x')
        self.obs_canvas.config(xscrollcommand=self.h.set)
        
        self.obs_canvas.place(x=130,y=50)
        self.obs_frame=Frame(self.obs_canvas,bg='green',width=1000,height=500, highlightbackground='black')
       
        self.obs_canvas.create_window((0,0),anchor=CENTER,window=self.obs_frame)
        
        
        
        #creates a button to add new obs
        self.add_obs=Button(self.main_frame,text='Add Chart',font=('ariel',12),command=self.add_entries)
        self.add_obs.place(x=700,y=2)
        
       
        
    def populate(self):
        '''populates the obs frame with obs entries'''
        
        self.time=Label(self.obs_frame,text=self.hr,font=('ariel',11),width=5)
        self.time.place(x=self.x,y=5)
        
        self.heartRate_entry=Entry(self.obs_frame,width=6,font=('ariel',11))
        self.heartRate_entry.place(x=self.x,y=43)
        
        self.bp_entry=Entry(self.obs_frame,width=6,font=('ariel',11)) 
        self.bp_entry.place(x=self.x,y=83)
        
        self.spo2_entry=Entry(self.obs_frame,width=6,font=('ariel',11)) 
        self.spo2_entry.place(x=self.x,y=123)
        
        self.temp_entry=Entry(self.obs_frame,width=6,font=('ariel',11)) 
        self.temp_entry.place(x=self.x,y=163)
        
        self.resp_entry=Entry(self.obs_frame,width=6,font=('ariel',11)) 
        self.resp_entry.place(x=self.x,y=203)
        
        self.pup_entry=Entry(self.obs_frame,width=6,font=('ariel',11)) 
        self.pup_entry.place(x=self.x,y=243)
        
        self.reaction_entry=Entry(self.obs_frame,width=6,font=('ariel',11)) 
        self.reaction_entry.place(x=self.x,y=283)
        
        self.time_inc()
        
    def add_old_entries(self):
        '''written to solve the bug of frame size increasing when i click the obs_chart button
        i only want it to increase to accomodate the number of old entries and after that not to increase again '''
        
        #get the number of old entries.
        num_old=self.config[hosp]['obs_count']
        num_old=int(num_old)
        #increase the size of the frame to accomodate the number of old entries.
        #1000 is the original size of the frame,multiply the number of old entries by 75 which is the 
        #size of each frame.
        self.obs_frame.config(width=(num_old *78))
        for i in range(num_old):
            self.populate()
            self.x+=75
            
        global x
        x=self.x
        self.obs_canvas.config(scrollregion=self.obs_canvas.bbox('all'))
        
        
    def add_entries(self):    
        '''creates entries for observations. obtains the size of the frame and increases it by 75, each time the button is clicked
        this creates a new instance of the self.populate(), and hence resets the self.x value.'''
        print(f'first self.inc {self.inc}')
        self.obs_frame.config(width=self.obs_frame.winfo_width()+self.inc)
        
        print(f'value of width {self.obs_frame.winfo_width()}')
        global x
        
        
        self.x=x
        
        self.populate()
        x+=75        
        self.updateCount_config('obs_count')
        
        self.obs_canvas.config(scrollregion=self.obs_canvas.bbox('all'))
       # self.inc+=10

        #to accomodate new entries we have to increase the width of obs frame the width of each obs box.
        
        #obtain the obs_count and increase by 1 everytime this function runs
        
        
        print(self.inc)
        
    def time_inc(self):
        
        self.hr+=100
        
        if self.hr>2400:
            self.hr-=2400
            
        #create a variable to check the number of time this function is called or the button is clicked
        #to call the function. i will call it self.number, my initial idea was to set it to 0 at the class but the problem is 
        
        #everytime i close and reopen it resets to 0, beats the purpose. deceided to save it to config.ini
    def updateCount_config(self,key):  
        '''updates the key of the config file to a new value , grabs the old value and increases it by 1 eachtime the 
        button is clicked and saves it.''' 
        self.config.read('config.ini')
        self.key=key
       
        self.old_value=int(self.config[hosp][self.key])
        self.old_value+=1
        self.config[hosp][self.key]=str(self.old_value)
        with open('config.ini','w') as configfile:
            self.config.write(configfile)
        
    def clear_frame(self):
        '''you have to clear the frame of all widget to be to pop new widgets inside.'''
        for frame in self.main_frame.winfo_children():
            frame.destroy()
       
    def create_nursing_frame(self):
        self.clear_frame()
        self.note_n_frame_y=10
        Label(self.main_frame,text='Nursing Notes',font=('verdana',15,'bold')).place(x=300,y=2)
       
        self.canvas=Canvas(self.main_frame,width=1200, height=500)
        self.canvas.place(x=5,y=50)
        self.nursing_frame=Frame(self.canvas,width=1200,height=500,bg='brown')
        
        self.canvas.create_window((0,0),anchor=CENTER,window=self.nursing_frame)
        
        self.scroll=Scrollbar(self.main_frame,orient='vertical',command=self.canvas.yview)
        self.scroll.pack(side='right',fill=Y)
        self.canvas.config(yscrollcommand=self.scroll.set)
        
        self.add_nursing_note=Button(self.main_frame,text='Add Note',command=self.new_nursing_note)
        self.add_nursing_note.place(x=500,y=2)
        self.readConfig_populate('nur_notes_count')
        
        #reset the self.note_n_frame_y value, to that the frame can start from the original y value, when you re-click, otherwise it starts from
        #the increase y value.
        
        print(f' y value from create frame {self.note_n_frame_y}')
        
        
    def new_nursing_note(self):
        '''Add nursing note when the button is clicked.'''
        print(f' y value before clicking add {self.note_n_frame_y}')
        self.today=datetime.now().strftime('%D %H:%M')
        self.note_frame=Frame(self.nursing_frame,bg='orange',width=900,height=500)
        self.note_frame.place(x=15,y=self.note_n_frame_y)
        
        Label(self.note_frame,text='Date and Time',font=('verdana',12)).place(x=5,y=50)
        Label(self.note_frame,text=self.today,font=('verdana',12)).place(x=180,y=50)
        Label(self.note_frame,text='Name of Nurse',font=('verdana',12)).place(x=5,y=85)
        
        
        
        nurse_name=Entry(self.note_frame,font=('verdana',12))
        nurse_name.place(x=180,y=85)
        Label(self.note_frame,text='Notes',font=('verdana',12)).place(x=5,y=200)
        nurse_note=Text(self.note_frame,width=50,height=15,font=('verdana',12))
        nurse_note.place(x=180,y=120)
        
        self.note_n_frame_y+=500     
        
        self.nursing_frame.config(height=self.nursing_frame.winfo_height()+500)
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        self.readConfig_Starttime('nur_note_starttime')
        self.updateCount_config('nur_notes_count')
        print(f' y value after clicking {self.note_n_frame_y}')
        
       
        
    def create_medical_frame(self):
        self.clear_frame()
        self.note_m_frame_y=10
        Label(self.main_frame,text='Medical Notes',font=('verdana',15,'bold')).place(x=300,y=2)
        self.add_medical_note=Button(self.main_frame,text='Add Note',command=self.new_medical_note)
        self.add_medical_note.place(x=500,y=2)
        
        self.canvas=Canvas(self.main_frame,width=1200, height=500)
        self.canvas.place(x=5,y=50)
        self.medical_frame=Frame(self.canvas,width=1200,height=500,bg='brown')
        
        self.canvas.create_window((0,0),anchor=CENTER,window=self.medical_frame)
        
        self.scroll=Scrollbar(self.main_frame,orient='vertical',command=self.canvas.yview)
        self.scroll.pack(side='right',fill=Y)
        self.canvas.config(yscrollcommand=self.scroll.set)
        self.readConfig_populate('med_notes_count')
        
        #reset the self.note_n_frame_y value, to that the frame can start from the original y value, when you re-click, otherwise it starts from
        #the increase y value.
        
        
        
        
     
        
    def new_medical_note(self):
        '''Adds medical note when the button is clicked'''
        self.today=datetime.now().strftime('%D %H:%M')
        
        self.note_frame=Frame(self.medical_frame,bg='orange',width=900,height=500)
        self.note_frame.place(x=10,y=self.note_m_frame_y)
        Label(self.note_frame,text='Date and Time',font=('verdana',12)).place(x=5,y=50)
        Label(self.note_frame,text=self.today,font=('verdana',12)).place(x=180,y=50)
        Label(self.note_frame,text='Name of Nurse',font=('verdana',12)).place(x=5,y=85)
        nurse_name=Entry(self.note_frame,font=('verdana',12))
        nurse_name.place(x=180,y=85)
        Label(self.note_frame,text='Notes',font=('verdana',12)).place(x=5,y=200)
        nurse_note=Text(self.note_frame,width=50,height=15,font=('verdana',12))
        nurse_note.place(x=180,y=120)
        
        self.note_m_frame_y+=500
        #self.nursing_frame_height+=300
        self.medical_frame.config(height=self.medical_frame.winfo_height()+500)
        self.canvas.config(scrollregion=self.canvas.bbox('all'))
        
        self.readConfig_Starttime('med_note_starttime')
        self.updateCount_config('med_notes_count')
        
        
        
        
    
    def drugs(self):
        pass
        print(self.x)
#creates an instance of the outline class.
chart=PatientChart()