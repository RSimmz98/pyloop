import pyautogui as pg
import time 

time.sleep(10) ## you can change it to whatever time that you want
txt = open('happbirthday.txt', 'r')
a = "Name of person"# e.g you .. you can change this part to whatever you want or remove it 

for i in txt:
    pg.write(a+'' +i)
    pg.press('Enter')

    #to make it easy make sure you put your txt fie in the same folder with your python file
   