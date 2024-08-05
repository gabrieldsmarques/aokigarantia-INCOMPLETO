        
import numpy, pyautogui, pandas, plotly
import time ##adiciona comandos de tempo, como pausas e tals
import pytesseract ##pytesseract serve pra reconhecer texto em imagens
from PIL import Image
from io import BytesIO

pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'  ##definindo o caminho até o pytesseract


pyautogui.PAUSE = 0.2 ## deixa um intervalo de tempo entre todos os códigos de pyautogui, pro código n fazer tudo rápido demais e o pc não acompanhar
pyautogui.sleep = 5
x, y, altura, largura = 360, 300, 500 , 1200 ##variavel com o tamanho desejado do print de inserir NÃO MUDAR
sgs=('sgs.txt')


tabela = pandas.read_csv('sucateamento.csv')


for linha in tabela.index: 
    #tirando print

    imagem_tela = pyautogui.screenshot(region=(x, y, altura, largura))
    imagem_tela = numpy.array(imagem_tela)

    #salvando em formato pillow pra mexer

    imagem_tela_pil = Image.fromarray(imagem_tela)

    # extraindo codigo

    codigo_extraido = pytesseract.image_to_string(imagem_tela_pil)

    #guardando o numero da peça em variável pra comparar
    codigo_procurado = tabela.loc[linha, "peca"]
    
    # if codigo_procurado in codigo_extraido:
    
    linhas = codigo_extraido.split('\n')
    
    # for linha in linhas
