##inserir na requisição é igual a x=60, y=331
##tipo de movimento na requisição é igual a x=95, y=361
##mercadorias na requisição é igual a x=124, y=225
## "+" da mercadorias na requisição é igual a x=87, y=325
##informações complementares na requisição é igual a x=223, y=226


##vendedor = x=70, y=716
##a cada 15 clicks tem q pegar uma nova coordenada?
##vendedor = x=69, y=1016

##   pyautogui.click(87, 325)

import pyautogui, sys, keyboard
import time


##parte pra definir as coisas essenciais do códiog, como ir até o final da página, alinhar tudo e a criação de variáveis.


pyautogui.PAUSE = 0.1
time.sleep(1)


pyautogui.scroll(-99999)
pyautogui.scroll(300)


clicks=0 
loops=0 ##define quantas vezes o loop de alinhamento foi feito, serve pra alinhar o alinhamento q zoa dps
pecas=195 ##quantas peças tem na requisição, importante colocar pra não quebrar o final
x= 65 #eixo x da tela (horizontal)
y= 1020 ##eixo y da tela (vertical)


##função que vai fazer tudo
def clicador():
    pyautogui.scroll(65)
    pyautogui.click(x, y)
    
    # pyautogui.doubleClick(272, 328)
    # pyautogui.write("VINI")
    # time.sleep(0.4)
    # pyautogui.press('enter')
    # time.sleep(0.5) 
    # pyautogui.click(940, 877)   
 
##loop pra utilizar a função infinitamente
while clicks < 6:
    if (clicks==5):##um if porque a cada 5 loops o y desalinha, esse if serve pra alinhar bonitinho e voltar pro loop
        pyautogui.scroll(-5)
        clicks -= 5
        loops+=1
        
    clicador()
    clicks+=1
    pecas -=1
    if loops ==5:
        pyautogui.scroll(-7)
        loops-=5
    if (pecas ==13):
        while pecas !=0:
            y - 50
            pecas-1 ##MEXER NESSA PARTE AINDA

        ##quando chega nas últimas peças n scrolla mais pra cima, pegar coordenadas ou algo do tipo
        ##sempre 12 peças no final
   

    


