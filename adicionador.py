

import pyautogui
import time ##adiciona comandos de tempo, como pausas e tals
import pandas
import plotly
import pytesseract ##pytesseract serve pra reconhecer texto em imagens
import cv2 ##o opencv serve pra ler e processar imagens
import thefuzz as fuzz ##serve pra comparar textos
from PIL import Image
from io import BytesIO

pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'  ##definindo o caminho até o pytesseract


pyautogui.PAUSE = 0.2 ## deixa um intervalo de tempo entre todos os códigos de pyautogui, pro código n fazer tudo rápido demais e o pc não acompanhar
pyautogui.sleep = 5
x, y, altura, largura = 360, 300, 500 , 1200 ##variavel com o tamanho desejado do print de inserir NÃO MUDAR
tabela = pandas.read_csv('sucateamento.csv')


for linha in tabela.index: 
    count = len(str(tabela.loc[linha, "sg"]))
    sg = str(tabela.loc[linha,"sg"]) ##criando a sg numa variável pra acelerar o processo de cortar os 2 numeros extra de sg
    num = str(tabela.loc[linha, "peca"]) ##transformando o numero da peça numa variável pra poder comparar depois
    if count==6:
        sg = sg[:4] ##transformando a linha numa variável pra facilitar a vida
    pyautogui.write(sg)
    pyautogui.press('enter')
    foto = pyautogui.screenshot(region=(x, y, altura, largura)) ##tira print da tela pra guardar na memória
    
    ##convertendo pra objeto bytesio pra manipular ela na memória e ser mais rápido
    
    foto_bytes = BytesIO()
    foto.save(foto_bytes, format='PNG')

    ##carregando a imagem
    
    foto_bytes.seek(0)
    imagem = Image.open(foto_bytes) 
    
    ##processando imagem
    
    imagem = imagem.convert('L')
    
    codigo = pytesseract.image_to_string(imagem) ##convertendo pra texto
    
    if codigo.strip() in 'sucateamento.csv':
        print('deu bom')
    else:
        print('nao deu')
    
    
    

    
    
    
