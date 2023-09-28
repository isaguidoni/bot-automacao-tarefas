# Passo a passo do projeto 
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

# pyautogri.click -> clicar com o mouse
# pyautogri.write -> escrever um texto 
# pyautogri.press -> apertar 1 tecla
# pyautogri.hotkey -> atalho (combinacao de teclas)
pyautogui.PAUSE = 0.3

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press ("enter")

# esperar o site carregar 
time.sleep(3)

# Passo 2: Fazer login 
# Passo 3: Importar a base de dados de produtos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos