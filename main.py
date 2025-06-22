import pyautogui as bot
import keyboard as kb
import time

time.sleep(3)
quantas_kills = 10000
sell = (569, 273)

# Você precisa de um client com keybind para usar esse macro.
# Após ter instalado um, configure o a tecla 'delete'
# para o seguinte comando '/armazem'

for i in range(quantas_kills):
    time.sleep(7)
    bot.leftClick()
    time.sleep(0.5)
    bot.hotkey('delete')
    time.sleep(0.5)
    bot.moveTo(sell)
    time.sleep(1)
    bot.leftClick()
