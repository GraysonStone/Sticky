
import datetime
import ToDo
from Tkinter import *




class Stick():
    colorarray=["#B6B6B4","#000000", "#FDD017","#FFFF00","#659EC7","#99C68E","#85BB65",
            "#357EC7","#C8B560","#6F4E37","#F9966B","#F88158","#C24641","#954535",
            "#E8ADAA","#E8ADAA","#5E5A80","#C8A2C8","#FFFFFF","#4E9258","#347235",
            "#3EA99F","#4C787E","#4863A0","#2B547E","#C6DEFF","#768EAF","#617C58",
            "#1B3612","#E2A76F","#BA7F47","#C36241","#EB8A69","#B38481","#7F4E52"]
    topcolor=""
    bgcolor=""
    textcolor=""
    dataArr=[]
    xlocation=""
    ylocation=""
    transparency=1.0
    noteMain=""
    invert=0

    def __init__(self):
        self.dataArr=[]
        self.noteMain=Tk()
        self.__getColor()
        self.__getData()
        self.__getXY()
        self.__window()

    def __getColor(self):

        f=open("/Users/Gray/Desktop/StickCharm/Color.txt","r")
        topcolor=f.readline()
        self.topcolor=topcolor[0:len(topcolor)-1]
        bgcolor=f.readline()
        self.bgcolor=bgcolor[0:len(bgcolor)-1]
        textcolor=f.readline()
        self.textcolor=textcolor[0:len(textcolor)-1]
        trans=f.readline()
        self.transparency=trans[0:len(trans)-1]
        f.close()
    def __getData(self):
        task=open("/Users/Gray/Desktop/StickCharm/Stickfo.txt","r")
        date=open("/Users/Gray/Desktop/StickCharm/StickDate.txt","r")
        inv=open("/Users/Gray/Desktop/StickCharm/invert.txt","r")
        self.invert=(inv.readline())
        self.invert=int(self.invert[0:len(inv.readline())-1])
        
        for line in task:
            dline=date.readline()
            td=ToDo.ToDo(line,dline)
            if(datetime.datetime(int(td.year),int(td.month),int(td.day))>(datetime.datetime.now())-datetime.timedelta(days=1)):
                self.dataArr.append(ToDo.ToDo(line,dline))
    
        inv.close()
        task.close()
        date.close()
        self.__fixData()
    def __fixData(self):
        task=open("/Users/Gray/Desktop/StickCharm/Stickfo.txt","w")
        date=open("/Users/Gray/Desktop/StickCharm/StickDate.txt","w")
        for i in range(0,len(self.dataArr)):
            task.write(self.dataArr[i].entry+'\n')
            date.write(self.dataArr[i].date+'\n')

        task.close()
        date.close()
    def __getXY(self):
        loc=open("/Users/Gray/Desktop/StickCharm/Location.txt","r")
        xlocation=loc.readline()
        self.xlocation=xlocation[0:len(xlocation)-1]
        ylocation=loc.readline()
        self.ylocation=ylocation[0:len(ylocation)-1]
    def __window(self):
        def exit(e):
            note.destroy()
        def on_enter(e):
            top.itemconfig(l,fill="black")
        def on_leave(e):
            top.itemconfig(l,fill="red")
        def on_enter_add(e):
            top.itemconfig(add,fill="grey",outline="grey")
        def on_leave_add(e):
            top.itemconfig(add,fill=self.topcolor,outline=self.topcolor)
        def on_enter_add2(e):
            top.itemconfig(add2,fill="grey",outline="grey")
        def on_leave_add2(e):
            top.itemconfig(add2,fill=self.topcolor,outline=self.topcolor)
        def StartMove(event):
            note.x = event.x
            note.y = event.y
        def StopMove(event):
            note.x = None
            note.y = None
        def OnMotion(event):
            deltax = event.x - note.x
            deltay = event.y - note.y
            x = note.winfo_x() + deltax
            y = note.winfo_y() + deltay
            note.geometry("+%s+%s" % (x, y))

        
        note=self.noteMain
        note.geometry('%dx%d+%d+%d' % (350,len(self.dataArr)*22+50, int(self.xlocation), int(self.ylocation)))

        note.overrideredirect(True)

        note.wait_visibility(note)
        note.wm_attributes('-alpha',self.transparency)
        h=self.bgcolor

        note.configure(background=self.bgcolor)
        top=Canvas(note,width=350,height=35,bg=self.topcolor,highlightthickness=0)
        top.bind("<ButtonPress-1>",StartMove)
        top.bind("<ButtonRelease-1>",StopMove)
        top.bind("<B1-Motion>",OnMotion)
        top.pack()
        body=Canvas(note,width=350,height=len(self.dataArr)*22+15,bg=self.bgcolor,highlightthickness=0)
        body.pack()

        

        l=top.create_oval(330, 10,340, 20, outline="red", fill="red", width=3)
        top.tag_bind(l,"<Button-1>",exit)
        top.tag_bind(l,"<Enter>",on_enter)
        top.tag_bind(l,"<Leave>",on_leave)

        add=top.create_oval(10, 10,20, 20, fill=self.topcolor,outline=self.topcolor, width=3)
        l1=top.create_line(11,15,19,15)
        l2=top.create_line(15,11,15,19)
        top.tag_bind(l1,"<Button-1>",self.__addEntry)
        top.tag_bind(l1,"<Enter>",on_enter_add)
        top.tag_bind(l1,"<Leave>",on_leave_add)
        top.tag_bind(l2,"<Button-1>",self.__addEntry)
        top.tag_bind(l2,"<Enter>",on_enter_add)
        top.tag_bind(l2,"<Leave>",on_leave_add)
        top.tag_bind(add,"<Button-1>",self.__addEntry)
        top.tag_bind(add,"<Enter>",on_enter_add)
        top.tag_bind(add,"<Leave>",on_leave_add)
        
        add2=top.create_oval(30, 10,40, 20, fill=self.topcolor,outline=self.topcolor, width=3)
        l12=top.create_line(31,15,39,15)
       
        top.tag_bind(l12,"<Button-1>",self.__delEntry)
        top.tag_bind(l12,"<Enter>",on_enter_add2)
        top.tag_bind(l12,"<Leave>",on_leave_add2)
        top.tag_bind(add2,"<Button-1>",self.__delEntry)
        top.tag_bind(add2,"<Enter>",on_enter_add2)
        top.tag_bind(add2,"<Leave>",on_leave_add2)

        for i in range(0,len(self.dataArr)):
            body.create_text(1,22*(i+1),text=self.dataArr[abs(self.invert*(len(self.dataArr)-1)-i)].entry,anchor='w',font=("Courier", 12))
            body.create_text(345,22*(i+1),text=self.dataArr[abs(self.invert*(len(self.dataArr)-1)-i)].date,anchor='e',font=("Courier", 12))
            body.create_line(0,22*(i+1)+10,350,22*(i+1)+10)
        
        note.mainloop()

    def __addEntry(self,event):
        def apply(event,day,month,year):
            task=e.get()
            dateLine=str(month)+'/'+str(day)+'/'+str(year)+'\n'
            self.dataArr.append(ToDo.ToDo(task+'\n',dateLine))
            i=0
            td=self.dataArr[0]
            while(datetime.datetime(int(td.year),int(td.month),int(td.day)))>datetime.datetime(year,month,day):
                i+=1
                td=self.dataArr[i]
                
            self.dataArr.insert(i,ToDo.ToDo(task+'\n',dateLine))
            del self.dataArr[-1]
            self.__fixData()
            add.destroy()
            self.noteMain.destroy()
            self.dataArr = []
            Stick()
        def on_enter(e,c):
            (labList[c]).config(bg="grey")
        def on_leave(e,c):
            (labList[c]).config(bg="white")
        daysInMonth=[31,28,31,30,3130,31,31,30,31,30,31]
        add=Tk()
        add.geometry('%dx%d+%d+%d' % (250,230,300,300))
        task=""
        e=Entry(add)
        e.place(x=30,y=10)
        now=datetime.datetime.now()
        calender=Canvas(add,width=200,height=160,highlightbackground="grey")
        calender.place(x=25,y=40)
        dayOfWeek=now.weekday()+1
        if dayOfWeek==7:
            dayOfWeek=0
        dayNumber=now.day
        month=now.month
        year=now.year
        c=0
        labList=[]
        for i in range(0,5):
            while dayOfWeek<7:
                dapp=str(dayNumber)
                if len(str(dayNumber))==1:
                    dapp=' '+str(dayNumber)
                l=Label(add,text=dapp)
                l.bind("<Enter>",lambda event,c=c: on_enter(event,c))
                l.bind("<Leave>",lambda event,c=c: on_leave(event,c))
                l.bind("<Button-1>",lambda event,dayNumber=dayNumber,month=month,year=year: apply(event,dayNumber,month,year))
                l.place(x=dayOfWeek*27+30,y=i*30+50)
                labList.append(l)
                dayNumber+=1
                dayOfWeek+=1
                c+=1
                if dayNumber>daysInMonth[month-1]:
                    dayNumber=1
                    month+=1
                    if month>12:
                        month=1
                        year+=1
            dayOfWeek=0
        add.mainloop()

    def __delEntry(self,event):
        def delete(e,c):
            del self.dataArr[c]
            delE.destroy()
            self.__fixData()
            self.noteMain.destroy()
            self.dataArr = []
            Stick()
        def on_enter(e,c):
            (delList[c]).config(bg="grey")
        def on_leave(e,c):
            (delList[c]).config(bg="white")
        delList=[]
        delE=Tk()
        delE.geometry('%dx%d+%d+%d' % (250, 30*len(self.dataArr)+30, 300, 300))
        for c in range(0,len(self.dataArr)):
            l = Label(delE, text=self.dataArr[c].entry)
            l.bind("<Enter>", lambda event, c=c: on_enter(event, c))
            l.bind("<Leave>", lambda event, c=c: on_leave(event, c))
            l.bind("<Button-1>", lambda event, c=c: delete(event, c))
            delList.append(l)
            l.place(x=10, y=c * 30 + 30)
        delE.mainloop()
def main():
    Stick()

if __name__ == '__main__':
    main()
