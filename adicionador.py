
import numpy
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
sgs=('sgs.txt')

tabela = pandas.read_csv('sucateamento.csv')

def leitura(sgs):
    try:
        with open(sgs, 'r') as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        return set()
    
def salvarleitura(sgs, codigo):
    with open(sgs, 'a') as f:
        f.write(f"{codigo}\n")
        
codigos_processados= leitura(sgs)

def verificar(codigo):
    if codigo not in codigos_processados:
        codigos_processados.add(codigo)
        salvarleitura(sgs, codigo)
        return True
    return False

def clicar(imagem_codigo):
    imagem_codigo_gray = cv2.cvtColor(imagem_codigo, cv2.COLOR_BGR2GRAY)
    imagem_tela_gray = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
    resultado = cv2.matchTemplate(imagem_tela_gray, imagem_codigo_gray, cv2.TM_CCOEFF_NORMED)
    
    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    return max_loc



    

for linha in tabela.index: 
    count = len(str(tabela.loc[linha, "sg"]))
    sg = str(tabela.loc[linha,"sg"]) ##criando a sg numa variável pra acelerar o processo de cortar os 2 numeros extra de sg
    num = str(tabela.loc[linha, "peca"]) ##transformando o numero da peça numa variável pra poder comparar depois
    if count==6:
        sg = sg[:4] ##transformando a linha numa variável pra facilitar a vida
    if verificar(sgs):
        pyautogui.write(sg)
        pyautogui.press('enter')
    
        foto = pyautogui.screenshot(region=(x, y, altura, largura)) ##tira print da tela pra guardar na memória
        
        ##convertendo pra objeto bytesio pra manipular ela na memória e ser mais rápido  
        foto_bytes = BytesIO()
        foto.save(foto_bytes, format='PNG')
        
        ##carregando a imagem  
        foto_bytes.seek(0)
        imagem = Image.open(foto_bytes) 
        
        
        
        
        ##CÁLCULO DO QUADRADO NO CÓDIGO
        
        ##PROCESSANDO IMAGEM
        imagem_tela = Image.open(imagem)
        imagem_tela = numpy.array(imagem_tela)
        imagem_tela = cv2.cvtColor(imagem_tela, cv2.COLOR_RGB2BGR)
        
        ##lENDO PRINT DO QUADRADO
        imagem_codigo = cv2.imread('quad.png')
        
        ##PEGANDO POSIÇÃO DO QUADRADO
        posicao_codigo = clicar(imagem_codigo, imagem_tela)
        
        #TAMANHO
        tamanho_quadrado = (16, 16)
        
        ##CALCULO DE POSIÇÃO
        largura_codigo, altura_codigo = imagem_codigo.shape[1], imagem_codigo.shape[0]
        x_centralizado = posicao_codigo[0] + largura_codigo // 2
        y_centralizado = posicao_codigo[1] + altura_codigo // 2
        
        x_click = x_centralizado + tamanho_quadrado[0] // 2
        y_click = y_centralizado + tamanho_quadrado[1] // 2
        
        
        
            
        ##processando imagem
        imagem = imagem.convert('L')
    
        codigo = pytesseract.image_to_string(imagem) ##convertendo pra texto 

        if codigo.strip() in 'sucateamento.csv':
            pyautogui.click(x=x_click, y=y_click)

    
    
    

    
    
    
