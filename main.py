# -*- coding: utf-8 -*-

#########################################################
#                                                       #
#                                                       #
#     created by BirdLQ: https://github.com/BirdLQ      #
#                                                       #   
#                                                       #
#########################################################


import sys, webbrowser, time, winsound, os

from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, ImageDraw
import PIL.Image

from win10toast import ToastNotifier
from pygame import mixer

#ini
window = Tk()
toaster = ToastNotifier()
mixer.init()
    
#wdw
window.title('Reveil')
w = 550
h = 400
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = int(ws/2.2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.resizable(False, False)
(width, height) = (550, 400)


class simpleAnimation:
    def __init__(self, animationOn):
        self.animationOn = animationOn
        self.size = 10
        self.im = PIL.Image.new( "RGB", (400, 400), (255, 255, 255) )
        self.photo = ImageTk.PhotoImage(self.im)
        self.label = Label(window, image=self.photo)
        self.label.image = self.photo
        self.label.pack()
        self.buttonHolder = Frame(window)
        self.buttonHolder.pack()
        self.animate()

    def interpolate(self, color_a, color_b, t):
        return tuple(int(a + (b - a) * t) for a, b in zip(color_a, color_b))

    def Application(self, *args, **kwargs):
        self.labelIntro = Label(window, text="CREATED BY\nBIRD LQ", font=('calibri', 36, 'bold'),
                            background = '#1b2836')
        self.labelIntro.place(relx=0.515, rely=0.45, anchor=CENTER)
        
        self.display_version = Label(window, text="VERSION: ALPHA (V2)", font=('calibri', 12, 'bold'), 
                        background = '#1b2836', 
                        foreground = '#fafafa')
        self.display_version.place(relx=0.725, rely=0.94, anchor=NW)

        self.label_background_8_bit_color = tuple((27, 40, 54))

        self.label_foreground_8_bit_color = tuple((250, 250, 250))

        self.start_color = self.label_background_8_bit_color
        self.end_color = self.label_foreground_8_bit_color

        self.duration_ms = 1000
        self.frames_per_second = 60
        self.ms_sleep_duration = 1500 // self.frames_per_second
        self.current_step = 0

        self.update_label()
        
    def update_label(self):
        self.t = (1.0 / self.frames_per_second) * self.current_step
        self.current_step += 1

        self.new_color = self.interpolate(self.start_color, self.end_color, self.t)
        self.labelIntro.configure(foreground="#%02x%02x%02x" % self.new_color)

        if self.current_step <= self.frames_per_second:
            window.after(self.ms_sleep_duration, self.update_label)


    def animate(self):
        self.newIm = PIL.Image.new( "RGB", (width, height), (0, 0, 0) )
        self.draw = ImageDraw.Draw(self.newIm)
        (cX, cY) = (width/2, height/2)
        self.draw.ellipse( [cX-self.size/3, cY-self.size/3, cX+self.size/3, cY+self.size/3], (27, 40, 54))
        self.photo = ImageTk.PhotoImage(self.newIm)
        self.label.configure(image = self.photo)
        self.label.image = self.photo
        if self.animationOn and self.size<=1100:
            self.size += 15
            self.label.after(10, self.animate)
        else:
            self.Application()
            self.labelIntro.after(3100, self.labelIntro.pack)

simpleAnimation(True)

def main():
#    def atime(): 
#        string = time.strftime('%H:%M:%S %p') 
#        lbl.config(text = string) 
#        lbl.after(1000, atime)
#        
#    lbl = Label(window, font = ('calibri', 40, 'bold'), 
#                background = '#1b2836', 
#                foreground = '#fafafa', anchor=N)
#    lbl.pack()
#    
#    atime()
  
    global state, display
    
    display = Label(window, textvariable="", font=('calibri', 78, 'bold'), 
                background = '#1b2836', 
                foreground = '#fafafa')
    display.config(text="00:00:00")
    display.place(relx=0.5, rely=0.22, anchor=CENTER)
    display.pack
    state = False

    def countdown():
        global state,hours,mins, secs
        
        if state == True:
            if hours == 0 and mins == 0 and secs == 0:
                display.config(text="DONE!",font = ('calibri', 92, 'bold'))
                state = False
                if link_open == "www.exemple.com" or link_open == "":
                    mixer.music.load("music")
                    mixer.music.play()
                else:
                    webbrowser.open(link_open)
            else:
                display.config(text="%02d:%02d:%02d" % (hours, mins, secs))
                
                if mins==0:
                    if hours!=0:
                        hours-=1
                        mins=59
                if secs == 0:
                    mins -= 1
                    secs = 59
                else:
                    secs -= 1


                window.after(1000, countdown)
                
    def start():
        global state, hours, mins, secs, link_open
        
        if state == False:
            state = True
            
            if not str(hourEntry.get()):
                hours = 0
            else:
                hours = int(hourEntry.get())
                
            if not str(minuteEntry.get()):
                mins = 0
            else:
                mins = int(minuteEntry.get())

            secs = 0
            
            if hours==0 and mins==0:
                messagebox.showinfo("Time Countdown","Saisie invalide")
                               
            else:
                countdown()

                lbl1.destroy()
                lbl2.destroy()
                lbl3.destroy()
                link_open = str(link.get())
                link.destroy()
                hourEntry.destroy()
                minuteEntry.destroy()
                
                display.place(y=display.winfo_y()+50)
                display.config(font = ('calibri', 92, 'bold'))
                    
                toaster.show_toast("Reveil", "Le décompte a commencé",
                                   threaded=True, icon_path=None, duration=5)

    lbl1=Label(window, text='Heure:')
    lbl1.config(font=("calibri", 15, 'bold'), background = '#1b2836', foreground = '#fafafa')
    
    lbl2=Label(window, text='Minute:')
    lbl2.config(font=("calibri", 15, 'bold'), background = '#1b2836', foreground = '#fafafa')
    
    lbl3=Label(window, text='Lien:')
    lbl3.config(font=("calibri", 15, 'bold'), background = '#1b2836', foreground = '#fafafa')
    
    link=Entry(window,bd=0, font=("arial",10,""), foreground = 'grey', 
               textvariable="")
    link.insert(0,"www.exemple.com")
    link.place(relx=0.48, rely=0.65, anchor=W)
    
    hourEntry= Entry(window, bd=0, width=10, font=("arial",10,""), foreground = 'grey', 
             textvariable="")
    hourEntry.insert(0,"00")
    hourEntry.place(relx=0.48, rely=0.45, anchor=W) 
    
    minuteEntry= Entry(window,bd=0, width=10, font=("arial",10,""), foreground = 'grey', 
               textvariable="")
    minuteEntry.insert(0,"00")
    minuteEntry.place(relx=0.48, rely=0.55, anchor=W)
    
    def supp_hour(event):       
        try:
            if int(hourEntry.get())<=1:
                event.widget.delete(0,"end")
        except:
            hourEntry.insert(0,"00")
            
    def supp_min(event):       
        try:  
            if int(minuteEntry.get())<=1:
                event.widget.delete(0,"end")
        except:
            minuteEntry.insert(0,"00")
            
    def supp_link(event):                 
        if str(link.get()) == "www.exemple.com":
            event.widget.delete(0,"end")
        if str(link.get())=="":
            link.insert(0,"www.exemple.com")
        
        return None

    hourEntry.bind("<Button-1>",supp_hour)
    minuteEntry.bind("<Button-1>",supp_min)
    link.bind("<Button-1>",supp_link)
    
    lbl1.place(relx=0.4, rely=0.45, anchor=CENTER) 
    lbl2.place(relx=0.4, rely=0.55, anchor=CENTER) 
    lbl3.place(relx=0.4, rely=0.65, anchor=CENTER) 
        
    def switch_button():
        def test(event):
            btn_state = win_btn['image']
            win_btn.config(image=mid_btn)
            if btn_state=='ON':
                display.destroy()
                main()
            else:
                start()             
            window.after(38, win_btn.config, {'image': off_btn if btn_state == 'ON' else on_btn}) 

        on_btn = PhotoImage(file='on.png', name='ON')
        mid_btn = PhotoImage(file='mid.png')
        off_btn = PhotoImage(file='off.png', name='OFF')

        win_btn = Label(window, image=off_btn)
        win_btn.place(relx=0.5, rely=0.85, anchor=CENTER)
        win_btn.config(bg='#1b2836', cursor='hand2')
        win_btn.bind("<Button-1>", test)
        #win_btn.pack()
            
    switch_button()


window.after(4200,main)

window.mainloop()
