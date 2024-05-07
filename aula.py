# passo a passo do projeto

# 1. abrir o sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
# para instalar: pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 1
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

time.sleep(2)

# 2. Fazer login

pyautogui.press("tab")#selecionou o butão login
time.sleep(2)
pyautogui.write("projeto@gmail.com")#escreveu email
time.sleep(0.5)

pyautogui.press("tab")#pulou para senha
pyautogui.write("qwertyuiop")#escreveu senha
time.sleep(0.5)

pyautogui.press("tab")#pulou para logar
pyautogui.press("enter")#entrou na pagina da empresa

# 3. Abrir/importar a base de dados de produtos para cadastrar

import pandas as pd
tabela = pd.read_csv("produtos.csv")
time.sleep(5)
# 4. cadastrar um produto
for linha in tabela.index:

    #clicar no campo de codigo
    pyautogui.click(x=548, y=263)
    # preencher o campo de codigo
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    #passar para o proximo
    pyautogui.press("tab")
    #colocar marca do produto
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    #passar para o tipo de produto
    pyautogui.press("tab")
    #escrever o tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    #pular para o proximo
    pyautogui.press('tab')
    #ecrever categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    #pular para o proximo
    pyautogui.press('tab')
    #ecrever preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    #pular para o proximo
    pyautogui.press('tab')
    #escrever custoMOLO000251   Logitech    Mouse   1   
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    #pular para o proximo
    pyautogui.press('tab')
    #escrever obs
    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press("enter")  
    pyautogui.scroll(5000)
        


# 5. Repetir isso tudo até acabar a lista de produtos