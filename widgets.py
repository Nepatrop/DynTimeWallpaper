from tkinter import *
from tkinter.ttk import *
from time import strftime
import datetime



root = Tk()
root['bg'] = '#fcfcfc'
root.overrideredirect(True)
root.resizable(False, False)
root.wm_attributes("-alpha", 0.7)
root.wm_attributes("-transparentcolor", "#fcfcfc")

windowTime = Label(root, font=('aerial', 50), background='#fcfcfc', foreground='#ffffff')
windowDate = Label(root, font=('aerial', 13), background='#fcfcfc', foreground='#ffffff')

days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
months = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'дек']

root.geometry('+300+200')


def NowTime():
    string = strftime('%H:%M')
    today = datetime.datetime.today()
    windowTime.config(text=string)
    windowDate.config(text=f'{days[today.weekday()]}, {months[int(today.strftime("%m")) - 1]} {today.day}')

    windowTime.after(1000, NowTime)


windowTime.pack(anchor='center')
windowDate.pack(anchor=N)

a = False

if a:
    windowTime.configure(background='#171717')

    def b1motion(win, e):
        win.geometry("+%d+%d" % (win.winfo_x() + e.x - win.start.x, win.winfo_y() + e.y - win.start.y))


    def motion(win, e):
        win.start = e


    windowTime.bind('<B1-Motion>', lambda e: b1motion(root, e))
    windowTime.bind('<Motion>', lambda e: motion(root, e))

NowTime()
mainloop()