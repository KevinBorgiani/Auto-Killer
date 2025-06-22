import customtkinter as ctk
import pyautogui as bot
import keyboard as kb
import time

time.sleep(3)
quantas_kills = 10000
sell = (569, 273)

# OBS: Pode ser que não funcione, porque a resolução da sua tela pode ser diferente da minha.
# A minha é: 1360x768, jogando em modo janela.

app = ctk.CTk()
app.geometry("300x300")
app.title("Auto-Killer")

titulo = ctk.CTkLabel(app, text="Aperte o botão para iniciar.", font=("Arial", 18))
titulo.pack(pady=20)

def iniciar():
    for i in range(quantas_kills):
        time.sleep(7)
        bot.leftClick()
        time.sleep(0.5)
        bot.hotkey('delete')
        time.sleep(0.5)
        bot.moveTo(sell)
        time.sleep(1)
        bot.leftClick()

def usar():
    app1 = ctk.CTk()
    app1.geometry("300x300")
    app1.title("Auto-Killer")

    titulo1 = ctk.CTkLabel(app1, text="Instale um client com mod de keybind.\nConfigure a tecla 'delete' para\no comando '/armazem'.\nInicie o macro.", font=("Bold", 16))
    titulo1.pack(pady=20)

    def fechar():
        app1.destroy()

    botao_fechar = ctk.CTkButton(app1, text="Fechar", command=fechar)
    botao_fechar.pack(pady=20)

    app1.mainloop()

botao_iniciar = ctk.CTkButton(app, text="Iniciar", command=iniciar)
botao_iniciar.pack(pady=20)


botao_comousar = ctk.CTkButton(app, text="Como usar", command=usar)
botao_comousar.pack(pady=20)

app.mainloop()
