import numpy as np
import pyautogui
import time
import pandas as pd
import pytesseract
import cv2
from PIL import Image
from io import BytesIO

# Configuring the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'

# PyAutoGUI configuration
pyautogui.PAUSE = 0.7  # Pause between commands
time.sleep(3)  # Wait 1 second for the screen to load
x, y, largura, altura = 360, 300, 1200, 500  # Screen capture area
sgs = 'sgs.txt'

# Loading the table of codes
tabela = pd.read_csv('sucateamento.csv')

# Functions for reading and saving processed codes
def leitura(sgs):
    try:
        with open(sgs, 'r') as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        return set()

def salvarleitura(sgs, codigo):
    with open(sgs, 'a') as f:
        f.write(f"{codigo}\n")

# Load previously processed codes
codigos_processados = leitura(sgs)

def verificar(codigo):
    if codigo not in codigos_processados:
        codigos_processados.add(codigo)
        salvarleitura(sgs, codigo)
        return True
    return False

def clicar(imagem_codigo, imagem_tela):
    # Converting images to grayscale
    imagem_codigo_gray = cv2.cvtColor(imagem_codigo, cv2.COLOR_BGR2GRAY)
    imagem_tela_gray = cv2.cvtColor(imagem_tela, cv2.COLOR_BGR2GRAY)

    # Template matching
    resultado = cv2.matchTemplate(imagem_tela_gray, imagem_codigo_gray, cv2.TM_CCOEFF_NORMED)

    _, _, _, max_loc = cv2.minMaxLoc(resultado)
    return max_loc

for linha in tabela.index:
    count = len(str(tabela.loc[linha, "sg"]))
    sg = str(tabela.loc[linha, "sg"])
    num = str(tabela.loc[linha, "peca"])
    if count == 6:
        sg = sg[:4]  # Adjusting the SG code to 4 digits

    if verificar(sg):
        pyautogui.write(sg)
        pyautogui.press('enter')
        

        # Capture the screen area
        foto = pyautogui.screenshot(region=(x, y, largura, altura))

        # Convert the screenshot to a NumPy array
        foto_bytes = BytesIO()
        foto.save(foto_bytes, format='PNG')
        foto_bytes.seek(0)
        imagem = Image.open(foto_bytes)

        # Convert the image to a format suitable for OpenCV
        imagem_tela = np.array(imagem)
        imagem_tela = cv2.cvtColor(imagem_tela, cv2.COLOR_RGB2BGR)

        # Load and process the template image
        imagem_codigo = cv2.imread('quad.png')
        if imagem_codigo is None:
            print("Error: Image file 'quad.png' not found.")
            continue

        # Get the position of the template in the screen capture
        posicao_codigo = clicar(imagem_codigo, imagem_tela)

        # Define the size of the clickable area
        tamanho_quadrado = (16, 16)

        # Calculate the click position
        largura_codigo, altura_codigo = imagem_codigo.shape[1], imagem_codigo.shape[0]
        x_centralizado = posicao_codigo[0] + largura_codigo // 2
        y_centralizado = posicao_codigo[1] + altura_codigo // 2

        x_click = x_centralizado + tamanho_quadrado[0] // 2
        y_click = y_centralizado + tamanho_quadrado[1] // 2

        # Process the image for OCR
        imagem = Image.fromarray(imagem_tela).convert('L')
        codigo = pytesseract.image_to_string(imagem).strip()

        # Check if the code is in the scrap list
        if codigo in tabela['sg'].values:
            pyautogui.click(x=x_click, y=y_click)
            print(f"Código {codigo} encontrado e clicado.")
        else:
            print(f"Código {codigo} não encontrado na lista de sucateamento.")