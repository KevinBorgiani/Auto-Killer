import pyautogui as bot
import keyboard as kb
import time

time.sleep(5)
quantas_kills = 10000
armazem = "/armazem"
sell_all = (713, 342)

for i in range(quantas_kills):
    time.sleep(10)
    bot.leftClick()
    time.sleep(1)
    bot.hotkey('enter')
    time.sleep(1)
    kb.write(armazem)
    time.sleep(1)
    bot.hotkey('enter')
    time.sleep(1)
    bot.moveTo(sell_all)
    time.sleep(1)
    bot.leftClick()
    
