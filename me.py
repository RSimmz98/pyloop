import pyautogui as pg
import time 

time.sleep(10)
txt = open('happbirthday.txt', 'r')
a = "happy birthday" 

for i in txt:
    pg.write(a+'' +i)
    pg.press('Enter')
   