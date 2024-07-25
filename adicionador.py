##pip install pyautogui (comando de instalação do pyautogui)
##pip install pandas (comando de instalação do pandas)

##pyautogui.click() -> clica na tela
##pyautogui.press() -> pressiona uma tecla
##pyautogui.write() -> escreve algo
##pyautogui.hotkey() -> pra usar atalhos do teclado

import pyautogui
import time ##adiciona comandos de tempo, como pausas e tals
import pandas
import plotly
import pytesseract ##pytesseract serve pra reconhecer texto em imagens
import cv2 ##o opencv serve pra ler e processar imagens
import thefuzz as fuzz ##serve pra comparar textos

pytesseract.pytesseract.tesseract_cmd = 'c:\Users\POSITIVO\AppData\Local\Programs\Python\Python312\Scripts\pytesseract.exe'  ##definindo o caminho até o pytesseract


pyautogui.PAUSE = 0.2 ## deixa um intervalo de tempo entre todos os códigos de pyautogui, pro código n fazer tudo rápido demais e o pc não acompanhar
pyautogui.sleep = 5

tabela = pandas.read_csv('sucateamento.csv')


for linha in tabela.index: 
    count = len(str(tabela.loc[linha, "sg"]))
    sg = str(tabela.loc[linha,"sg"]) ##criando a sg numa variável pra acelerar o processo de cortar os 2 numeros extra de sg
    num = str(tabela.loc[linha, "peca"]) ##transformando o numero da peça numa variável pra poder comparar depois
    if count==6:
        sg = sg[:4] ##transformando a linha numa variável pra facilitar a vida
    pyautogui.write(sg)
    pyautogui.press('enter')
    image = pyautogui.screenshot() ##tira print da tela pra guardar na memória
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ##converte a imagem pra cinza pra acelerar o processo de identificação do texto
    ret, thresh = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO) ##mais processamento de imagem pra acelerar o processo
    codigo= pytesseract.image_tostring(img)
    if fuzz.ratio(num, codigo) > 90: ##comparar o codigo da peça do print com o da tabela
        pyautogui.locateOnScreen()
    
    
    
