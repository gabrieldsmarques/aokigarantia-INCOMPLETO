##inserir na requisição é igual a x=60, y=331
##tipo de movimento na requisição é igual a x=95, y=361
##mercadorias na requisição é igual a x=124, y=225
## "+" da mercadorias na requisição é igual a x=87, y=325
##informações complementares na requisição é igual a x=223, y=226


##vendedor = x=70, y=716
##a cada 15 clicks tem q pegar uma nova coordenada?
##vendedor = x=69, y=1016



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

   

    


