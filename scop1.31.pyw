
import datetime
import ToDo
from Tkinter import *
from AppKit import NSScreen



class Stick():
    colorarray = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
              'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
              'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
              'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
              'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
              'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
              'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
              'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
              'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
              'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
              'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
              'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
              'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
              'indian red', 'saddle brown', 'sandy brown',
              'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
              'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
              'pale violet red', 'maroon', 'medium violet red', 'violet red',
              'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
              'thistle', 'snow2', 'snow3',
              'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
              'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
              'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
              'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
              'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
              'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
              'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
              'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
              'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
              'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
              'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
              'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
              'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
              'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
              'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
              'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
              'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
              'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
              'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
              'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
              'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
              'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
              'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
              'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
              'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
              'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
              'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
              'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
              'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
              'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
              'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
              'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
              'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
              'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
              'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
              'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
              'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
              'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
              'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
              'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
              'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
              'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
              'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
              'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
              'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
              'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
              'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
              'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
              'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
              'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
              'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
              'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
              'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
              'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
              'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
              'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
              'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']
    topcolor=""
    bgcolor=""
    textcolor=""
    dataArr=[]
    xlocation=""
    ylocation=""
    transparency=1.0
    noteMain=""
    invert=0
    colorVal=0
    

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
    def __fixColors(self):
        f=open("/Users/Gray/Desktop/StickCharm/Color.txt","w")
        f.write(self.topcolor+'\n')
        f.write(self.bgcolor+'\n')
        f.write(self.textcolor+'\n')
        f.write(self.transparency+'\n')
        f.close()
    def __fixLoc(self):
        loc=open("/Users/Gray/Desktop/StickCharm/Location.txt","w")
        loc.write(str(self.xlocation)+'\n')
        loc.write(str(self.ylocation)+'\n')
        loc.close()
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
        def on_enter_set(e):
            top.itemconfig(settings,fill="grey",outline="grey")
        def on_leave_set(e):
            top.itemconfig(settings,fill=self.topcolor,outline=self.topcolor)
        
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
        
        settings=top.create_oval(50, 10,60, 20, fill=self.topcolor,outline=self.topcolor, width=3)
        setCirc=top.create_oval(52, 12,58, 18, fill="black", width=0)
        
        top.tag_bind(settings,"<Button-1>",self.__setEntry)
        top.tag_bind(settings,"<Enter>",on_enter_set)
        top.tag_bind(settings,"<Leave>",on_leave_set)
        top.tag_bind(setCirc,"<Button-1>",self.__setEntry)
        top.tag_bind(setCirc,"<Enter>",on_enter_set)
        top.tag_bind(setCirc,"<Leave>",on_leave_set)
        
        
        for i in range(0,len(self.dataArr)):
            body.create_text(1,22*(i+1),text=self.dataArr[abs(self.invert*(len(self.dataArr)-1)-i)].entry,anchor='w',font=("Courier", 12),fill=self.textcolor)
            body.create_text(345,22*(i+1),text=self.dataArr[abs(self.invert*(len(self.dataArr)-1)-i)].date,anchor='e',font=("Courier", 12),fill=self.textcolor)
            body.create_line(0,22*(i+1)+10,350,22*(i+1)+10,fill=self.textcolor)
        
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
            
            

    def __setEntry(self,event):
        def color_change(e,color):
            if self.colorVal==0:
                self.bgcolor=color
            elif self.colorVal==1:
                self.topcolor=color
            elif self.colorVal==2:
                self.textcolor=color
            self.__fixColors()
            self.noteMain.destroy()
            sett.destroy()
            Stick()
        def body_sett():
            body.configure(bg="blue")
            self.colorVal=0
        def top_sett():
            self.colorVal=1
        def text_sett():
            self.colorVal=2
        def trans_sett():
            def get():
                self.transparency=str((w.get())/100.0)
                self.__fixColors()
                tran.destroy()
                sett.destroy()
                self.noteMain.destroy()
                Stick()
            tran=Tk()
            tran.geometry('%dx%d+%d+%d' % (150, 90, 300, 300))
            w=Scale(tran,from_=1,to=100,orient=HORIZONTAL)
            w.set(float(self.transparency)*100)
            w.place(x=5,y=5)
            App=Button(tran,text="Apply",command=get)
            App.place(x=20,y=50)
        def startloc_sett():
            def set():
                self.xlocation=int((w.get()/100.0)*width)
                self.ylocation=int((w2.get()/100.0)*height)
                self.__fixLoc()
                place.destroy()
                sett.destroy()
                self.noteMain.destroy()
                Stick()
            width=NSScreen.mainScreen().frame().size.width-350
            height=NSScreen.mainScreen().frame().size.height-200
            place=Tk()
            place.geometry('%dx%d+%d+%d' % (300,300, 310, 310))
            w=Scale(place,from_=0,to=100,orient=HORIZONTAL,length=230,resolution=0.1)
            w.set(float((float(self.xlocation)/float(width))*100))
            w.place(x=50,y=5)
            w2=Scale(place,from_=0,to=100,length=230,resolution=0.1)
            w2.set(float((float(self.ylocation)/float(height))*100))
            w2.place(x=5,y=50)
            app=Button(place,text="Apply",command=set)
            app.place(x=230,y=250)
        
        sett=Tk()
        sett.geometry('%dx%d+%d+%d' % (300, 380, 300, 300))
        body=Button(sett,text="Body",command=body_sett)
        body.place(x=5,y=2)
        top=Button(sett,text="Top",command=top_sett)
        top.place(x=65,y=2)
        text=Button(sett,text="Text",command=text_sett)
        text.place(x=115,y=2)
        tranparency=Button(sett,text="Trans",command=trans_sett)
        tranparency.place(x=170,y=2)
        startloc=Button(sett,text="Start",command=startloc_sett)
        startloc.place(x=233,y=2)
        for i in range(0,len(self.colorarray)):
            color=self.colorarray[i]
            l=Label(sett,text=" ",bg=self.colorarray[i])
            l.bind("<Button-1>",lambda e,color=color:color_change(e,color))
            l.place(x=(i%30)*10,y=(i/30)*22+30)
        sett.mainloop()

def main():
    Stick()

if __name__ == '__main__':
    main()
