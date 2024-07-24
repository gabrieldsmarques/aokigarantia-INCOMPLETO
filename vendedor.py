import pyautogui, sys, keyboard
import time

##função que vai fazer tudo
def clicador():
    pyautogui.scroll(65)
    pyautogui.click(x=69, y=1016)
    

##parte pra definir as coisas essenciais do códiog, como ir até o final da página, alinhar tudo e a criação de variáveis.
pyautogui.PAUSE =0.2
pyautogui.sleep =3
pyautogui.scroll(-9999999)
pyautogui.scroll(285)
clicks=0

    
        
##loop pra utilizar a função infinitamente
while clicks < 21:
    clicador()
    clicks+=1
    if (clicks==21):##um if porque a cada 21 loops o y desalinha, esse if serve pra alinhar bonitinho e voltar pro loop
        pyautogui.scroll(35)
        clicks -= 21
        clicador()

   

    


