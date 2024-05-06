# passo a passo do projeto

# 1. abrir o sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
# para instalar: pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 1.5
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado 
# pyautogui.hotkey -> apetar um conjunto de taclas (Ctrl, Ctrl v, Alt Tab)

# abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar nos site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#tempo de espera

time.sleep(1)

# 2. Fazer login

pyautogui.press("tab")#selecionou o butão login
pyautogui.write("projeto@gmail.com")#escreveu email
time.sleep(0.5)

pyautogui.press("tab")#pulou para senha
pyautogui.write("qwertyuiop")#escreveu senha
time.sleep(0.5)

pyautogui.press("tab")#pulou para logar
pyautogui.press("enter")#entrou na pagina da empresa

# 3. Abrir/importar a base de dados de produtos para cadastrar
import pandas as pd
pd.read_csv("produtos.csv")
# 4. cadastrar um produto
# 5. Repetir isso tudo até acabar a lista de produtos