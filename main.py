import sys, webbrowser, time
from tkinter import *
from time import strftime
import datetime
from tkinter import messagebox
from PIL import ImageTk, ImageDraw
import PIL.Image
from win10toast import ToastNotifier

window = Tk()
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

"""toaster = ToastNotifier()

display = Label(window, textvariable="", font=('calibri', 40, 'bold'), 
            background = '#1b2836', 
            foreground = '#fafafa')
display.config(text="00:00:00")
display.place(relx=0.5, rely=0.26, anchor=CENTER)
state = False

def countdown():
    global state,hours,mins, secs
    
    if state == True:

        if hours == 0 and mins == 0 and secs == 0:
            display.config(text="Done!",font = ('calibri', 40, 'bold'))
            state = False
            webbrowser.open(str(t3.get()))
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
    global state, hours, mins, secs
    if state == False:
        state = True
        hours = int(hourEntry.get())
        mins = int(minuteEntry.get())
        secs = 0
        if not str(t3.get()):
            messagebox.showinfo("Time Countdown","Please input a valid link")
        else:
            countdown()
            toaster.show_toast("Reveil", "Le décompte a commencé",
                               threaded=True, icon_path=None, duration=5)
        

lbl1=Label(window, text='Heure:')
lbl1.config(font=("calibri", 15, 'bold'), background = '#1b2836', foreground = '#fafafa')

lbl2=Label(window, text='Minute:')
lbl2.config(font=("calibri", 15, 'bold'), background = '#1b2836', foreground = '#fafafa')

lbl3=Label(window, text='Lien:')
lbl3.config(font=("calibri", 15, 'bold'), background = '#1b2836', foreground = '#fafafa')

t3=Entry(bd=0)
hourEntry= Entry(window,bd=0, width=10, font=("arial",10,""), 
         textvariable="") 
hourEntry.place(relx=0.48, rely=0.45, anchor=W)

minuteEntry= Entry(window,bd=0, width=10, font=("arial",10,""), 
           textvariable="") 
minuteEntry.place(relx=0.48, rely=0.55, anchor=W)

lbl1.place(relx=0.4, rely=0.45, anchor=CENTER)

lbl2.place(relx=0.4, rely=0.55, anchor=CENTER)

lbl3.place(relx=0.4, rely=0.65, anchor=CENTER)

t3.place(relx=0.48, rely=0.65, anchor=W)

b1=Button(window, bd=0,relief="groove", text='Activer', font=('calibri',12, 'bold'), cursor='hand2', command=start)
b1.place(relx=0.5, rely=0.85, anchor=CENTER)  

def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time)
    
lbl = Label(window, font = ('calibri', 40, 'bold'), 
            background = '#1b2836', 
            foreground = '#fafafa', anchor=N)
lbl.pack()

time()"""

size = 10
animationOn = False

def interpolate(color_a, color_b, t):
    return tuple(int(a + (b - a) * t) for a, b in zip(color_a, color_b))

def Application(*args, **kwargs):
    global frames_per_second, current_step, start_color, end_color, labelIntro, ms_sleep_duration

    labelIntro = Label(window, text="CREATED BY\nBIRD LQ", font=('calibri', 36, 'bold'),
                        background = '#1b2836')
    labelIntro.place(relx=0.515, rely=0.45, anchor=CENTER)
    
    display_version = Label(window, text="VERSION: ALPHA (V2)", font=('calibri', 12, 'bold'), 
                    background = '#1b2836', 
                    foreground = '#fafafa')
    display_version.place(relx=0.725, rely=0.94, anchor=NW)

    start_color = tuple((27, 40, 54))
    end_color = tuple((250, 250, 250))

    duration_ms = 1000
    frames_per_second = 60
    ms_sleep_duration = 1600 // frames_per_second
    current_step = 0

    update_label()
    
def update_label():
    global frames_per_second, current_step

    t = (1.0 / frames_per_second) * current_step
    current_step += 1

    new_color = interpolate(start_color, end_color, t)
    labelIntro.configure(foreground="#%02x%02x%02x" % new_color)

    if current_step <= frames_per_second:
        window.after(ms_sleep_duration, update_label)

def simpleAnimation():
    global label, height, width, buttonHolder
    im = PIL.Image.new( "RGB", (400, 400), (255, 255, 255) )
    photo = ImageTk.PhotoImage(im)
    label = Label(window, image=photo)
    label.image = photo
    label.pack()
    buttonHolder = Frame(window)
    buttonHolder.pack()
    animate()

def animate():
    global size, label, width, height, animationOn, intro
    newIm = PIL.Image.new( "RGB", (width, height), (0, 0, 0) )
    draw = ImageDraw.Draw(newIm)
    (cX, cY) = (width/2, height/2)
    draw.ellipse( [cX-size/3, cY-size/3, cX+size/3, cY+size/3], (27, 40, 54))
    photo = ImageTk.PhotoImage(newIm)
    label.configure(image = photo)
    label.image = photo
    if animationOn and size<=1100:
        size += 15
        label.after(10, animate)
    else:
        Application()
        labelIntro.after(3100, labelIntro.pack)

animationOn = True
simpleAnimation()

window.mainloop()