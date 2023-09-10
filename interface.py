import time
from tkinter import *
from loader import DoLoad
import tkinter.ttk as ttk
import tkinter.font as font
import os
import win32com.client
import webbrowser
import datetime



def Direction():
    path = rf'{os.path.abspath(os.getcwd())}'
    webbrowser.open(path)


def AddPack():
    path = rf'{os.path.abspath(os.getcwd())}\packages'
    webbrowser.open(path)


def Choice(event):
    name = event.widget.cget('text')
    with open("data/pack.txt", "w+") as choice_file:
        choice_file.write(name)
        choice_file.close()
    os.system("taskkill /F /IM DTW.exe")
    os.system('start "" /high "DTW.exe"')


def Autoload():
    global countA

    if countA % 2 == 0:
        autoload.config(image=on)
        text2.config(text='ON')

        way = os.environ.get('USERPROFILE') + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
        path = rf"{way}\DynTimeWallpaper.lnk"
        target = rf"{os.path.abspath(os.getcwd())}\DynTimeWallpaper.exe"
        work_dir = rf"{os.path.abspath(os.getcwd())}"

        shell = win32com.client.Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = work_dir
        shortcut.save()

    if countA % 2 == 1:
        autoload.config(image=off)
        text2.config(text='OFF')
        os.remove(os.environ.get('USERPROFILE') + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\DynTimeWallpaper.lnk")
    countA += 1


def Library():
    library_frame.place(x=220, y=0)
    settings_frame.place_forget()

    library.configure(background='#505050', activeforeground='white', activebackground='#505050')
    settings.configure(background='#1f1f1f')
    stick.place(x=2, y=40)

    xP = 0
    yP = 0
    with open("packages/config.txt", 'r') as file:
        for item in file:
            if xP <= 3:
                btn = Button(library_frame, text=item, background='#171717', anchor=S, activebackground='#2d586e', compound=TOP,
                             image=buttonsImage, font='Arial 10 bold', cursor='hand2', bd=0, fg='white', activeforeground='white')
                btn.bind('<Button>', Choice)
                btn.place(x=12 + xP*222, y=12 + yP*150)
                xP += 1
                if xP == 3:
                    yP += 1
                    xP = 0
        addPack = Button(library_frame, text="+", width=8, height=2, background='#171717', activebackground='#2d586e',
                         font='Arial 25', relief=RAISED, cursor='hand2', bd=0, fg='white', activeforeground='white', command=AddPack)
        addPack.place(x=33 + xP * 222, y=20 + yP * 150)


def Settings():
    library_frame.place_forget()
    settings_frame.place(x=220, y=0)

    library.configure(background='#1f1f1f')
    settings.configure(background='#505050', activeforeground='white', activebackground='#505050')
    stick.place(x=2, y=90)

    text1 = Label(settings_frame)
    text1.configure(text="Запуск с Windows", bg='#171717', bd=0, fg='white', font='Arial 11 bold')
    text3 = Label(settings_frame)
    text3.configure(text="Внимание! В связи со своими техническими требованиями приложение запускается одновременно\nс Windows в  ВЫСОКОМ приоритете для ядра, что может приводить к ошибкам.",
                    bg='#171717', bd=0, fg='white', font='Helvetica 9', justify=LEFT)

    text4 = Label(settings_frame)
    text4.configure(text="Директория приложения:", bg='#171717', bd=0, fg='white', font='Helvetica 11 bold')
    direct = Label(settings_frame)
    direct.configure(bg='#505050', text=os.path.abspath(os.getcwd()), foreground='white', font='Helvetica 11', width=40, anchor=W)
    directBut = Button(settings_frame, bg='#171717', image=dirImage, bd=0, activebackground='#171717', relief=RAISED, cursor='hand2', command=Direction)

    text5 = Label(settings_frame)
    text5.configure(text="Здесь могла быть ваша реклама", bg='#171717', bd=0, fg='white', font='Helvetica 6')

    text6 = Label(settings_frame)
    text6.configure(text="Для добавления своего пакета обоев:\n1. В папке packages создать папку и добавить её название в day.txt.\n2. Внутри создать папки day и night.\n3. В папке day располагаются изображения день+закат (до захода солнца),\nnight - ночь+рассвет (до первых лучей).\n4. Нумерация изображений от 0 до N.\n5. Поддерживаются изображения в форматах png, jpg, jpeg.",
                    bg='#171717', bd=0, fg='white', font='Consolas 11', anchor=S, justify=LEFT)

    text1.place(x=20, y=55)
    autoload.place(x=16, y=83)
    text2.place(x=85, y=89)
    text3.place(x=20, y=125)
    text4.place(x=20, y=185)
    direct.place(x=20, y=210)
    directBut.place(x=390, y=208)
    text5.place(x=550, y=0)
    text6.place(x=20, y=280)


way = os.environ.get('USERPROFILE') + "\\Desktop"
path = rf"{way}\DynTimeWallpaper.lnk"

if not os.path.exists(path):
    target = rf"{os.path.abspath(os.getcwd())}\DTW_interface.exe"
    work_dir = rf"{os.path.abspath(os.getcwd())}"

    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = work_dir
    shortcut.save()


root = Tk()
root['bg'] = 'black'
root.title('DynTimeWallpaper')
root.geometry(f'900x600+{int((root.winfo_screenwidth() / 2) - 450)}+{int((root.winfo_screenheight() / 2) - 300)}')
root.iconbitmap('resources/icon.ico')
root.resizable(False, False)

library_frame = Frame(relief=SOLID, width=680, height=600, bg='#171717')
settings_frame = Frame(relief=SOLID, width=680, height=600, bg='#171717')
menu = Frame(relief=SOLID, width=220, height=600, bg='#1f1f1f')

menu.pack(anchor=W)
stick = Canvas(menu, width=0.1, height=31)

sunrisePhoto = PhotoImage(file='resources/sunrise.png')
sunriseImage = sunrisePhoto.subsample(4, 4)
sunriseLabel = Label(menu, image=sunriseImage, borderwidth=0)

with open("data/day.txt", 'r') as file:
    day = file.read().replace('\n', '')
    now = str(datetime.datetime.now().day)
    file.close()

if now != day:
    with open("data/day.txt", "w+") as config_file:
        config_file.write(now)
        config_file.close()

    DoLoad()

with open("data/city.txt", 'r') as fileS:
    city = fileS.read().replace('\n', '')

textrise = Label(menu)
with open("data/sunrise.txt", 'r') as fileR:
    data = int(fileR.read().replace('\n', ''))
    sunriseDT = datetime.datetime.fromtimestamp(data)
    fileR.close()
if sunriseDT.minute < 10:
    srm = '0' + str(sunriseDT.minute)
else:
    srm = sunriseDT.minute
textrise.configure(text=f'{sunriseDT.hour}:{srm}', bg='#1f1f1f', bd=0, fg='white', font='Helvetica 14')
textrise.place(x=48, y=7)

textset = Label(menu)
with open("data/sunset.txt", 'r') as fileS:
    data = int(fileS.read().replace('\n', ''))
    sunsetDT = datetime.datetime.fromtimestamp(data)
    fileS.close()
if sunsetDT.minute < 10:
    ssm = '0' + str(sunsetDT.minute)
else:
    ssm = sunsetDT.minute
textset.configure(text=f'{sunsetDT.hour}:{ssm}', bg='#1f1f1f', bd=0, fg='white', font='Helvetica 14')
textset.place(x=158, y=7)

textCity = Label(menu)
textCity.configure(text=f'Локация:\n{city}', bg='#1f1f1f', bd=0, fg='white', font='Helvetica 12', anchor=W, justify=LEFT)
textCity.place(x=10, y=550)

sunsetPhoto = PhotoImage(file='resources/sunset.png')
sunsetImage = sunsetPhoto.subsample(4, 4)
sunsetLabel = Label(menu, image=sunsetImage, borderwidth=0)
sunriseLabel.place(x=10, y=3)
sunsetLabel.place(x=120, y=3)
dirPhoto = PhotoImage(file='resources/dir.png')
dirImage = dirPhoto.subsample(2, 2)

bF = font.Font(family='TkMenuFont', size=14)
buttonsPhoto = PhotoImage(file='resources/back.png')
buttonsImage = buttonsPhoto.subsample(5, 6)

library = Button(menu, text="Библиотека", bg='#1f1f1f', fg='white', bd=0, font=bF, width=23,
                 command=Library, cursor='hand2', activebackground='#1f1f1f', activeforeground='white', anchor=W, relief=SUNKEN)
library.place(x=5, y=40)
settings = Button(menu, text="Настройки", bg='#1f1f1f', fg='white', bd=0, font=bF, width=23,
                  command=Settings, cursor='hand2', activebackground='#1f1f1f', activeforeground='white', anchor=W, relief=SUNKEN)
settings.place(x=5, y=90)

on = PhotoImage(file="resources/on.png").subsample(3, 3)
off = PhotoImage(file="resources/off.png").subsample(3, 3)

text2 = Label(settings_frame)
text2.configure(bg='#171717', bd=0, fg='white', font='Arial 11')

if os.path.exists(os.environ.get('USERPROFILE') + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\DynTimeWallpaper.lnk"):
    countA = 1
    autoImage = on
    text2.configure(text="ON")
else:
    countA = 0
    autoImage = off
    text2.configure(text="OFF")

autoload = Button(settings_frame, image=autoImage, relief=SUNKEN, bg='#171717', command=Autoload, bd=0, activebackground='#171717', cursor='hand2')

Library()
root.mainloop()