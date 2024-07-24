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

pyautogui.PAUSE = 0.5 ## deixa um intervalo de tempo entre todos os códigos de pyautogui, pro código n fazer tudo rápido demais e o pc não acompanhar

colunas= [4]
tabela = pandas.read_excel('sucateamento.xlsx', usecols= colunas)

print(tabela)
