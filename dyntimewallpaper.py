import ctypes
import os
import datetime
import time
from loader import DoLoad



def TimeReturner():
    return datetime.datetime.now()


def ImageEditor(directory, imageNum):
    ext = ''
    if os.path.exists(f'{directory}\\{imageNum}.png'):
        ext = '.png'
    elif os.path.exists(f'{directory}\\{imageNum}.jpg'):
        ext = '.jpg'
    elif os.path.exists(f'{directory}\\{imageNum}.jpeg'):
        ext = '.jpeg'
    userWay = os.path.dirname(os.path.realpath(__file__))
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{userWay}\\{directory}\\{imageNum}{ext}', 3)


def DynTimeWallpaper(working):
    with open("data/pack.txt", 'r') as file:
        pack = file.read().replace('\n', '')
        folder = f'packages\\{pack}'
        file.close()

    dayFol = f'{folder}\\day'
    dayCount = len(os.listdir(dayFol))
    nightFol = f'{folder}\\night'
    nightCount = len(os.listdir(nightFol))

    while working:
        with open("data/day.txt", 'r') as file:
            day = file.read().replace('\n', '')
            now = str(datetime.datetime.now().day)
            file.close()

        if now != day:
            with open("data/day.txt", "w+") as config_file:
                config_file.write(now)
                config_file.close()
            DoLoad()

        with open("data/sunrise.txt", "r") as sunriseF:
            sunriseDT = int(sunriseF.read().replace('\n', ''))
            sunriseD = datetime.datetime.fromtimestamp(sunriseDT)
            sunrise = sunriseD.hour * 3600 + sunriseD.minute * 60
            sunriseF.close()

        with open("data/sunset.txt", "r") as sunsetF:
            sunsetDT = int(sunsetF.read().replace('\n', ''))
            sunsetD = datetime.datetime.fromtimestamp(sunsetDT)
            sunset = sunsetD.hour * 3600 + sunsetD.minute * 60
            sunsetF.close()

        print(sunset, sunrise)
        dayTime = sunset - sunrise
        nightTime = 86400 - dayTime

        dayStep = round(dayTime / dayCount)
        nightStep = round(nightTime / nightCount)

        nowTime = TimeReturner().hour * 3600 + TimeReturner().minute * 60 + TimeReturner().second
        sleepTime = 1

        while nowTime < sleepTime + nowTime:

            if (nowTime >= sunrise) and (nowTime < sunset):
                step = dayStep
                image = (nowTime - sunrise) // step
                sleepTime = (step * (image + 1) + sunrise) - nowTime
                fol = dayFol
            else:
                step = nightStep
                if (nowTime > sunrise) and (nowTime <= 86400):
                    image = (nowTime - sunset) // step
                    sleepTime = (step * (image + 1) + sunset) - nowTime
                else:
                    image = nowTime // step
                    sleepTime = (step * (image + 1)) - nowTime
                    if pack == "Minecraft" or pack == "Destiny 2":
                        image += 36
                fol = nightFol

            ImageEditor(fol, int(image))
            if sleepTime % 10 == 0:
                time.sleep(1)
            else:
                time.sleep(sleepTime % 10)
            nowTime = TimeReturner().hour * 3600 + TimeReturner().minute * 60 + TimeReturner().second