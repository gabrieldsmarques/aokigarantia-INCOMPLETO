import pyautogui
import time

# variáveis pro programa rodar
PAUSE_DURATION = 0.7 # define uma pausa entre comandos, aumentar caso o sistema/internet esteja lento
INITIAL_SCROLL_DOWN = -9999999 ##variável pra ir pro final da página
INITIAL_SCROLL_UP = 350 ##variável pra alinhar depois de ir pro final(NÃO MUDAR)
SCROLL_UP_AMOUNT = 45 ##define quanto a tela sobe depois de cada click (NÃO MUDAR)
MAX_CLICKS_BEFORE_REALIGN = 9 ##limite de clicks pra alinhar a tela (NÃO MUDAR)
PIECE_COUNT = 195 ##define quantas peças tem na requisição 
REALIGN_SCROLL_UP = 4  # define o quanto a tela vai descer pra alinhar (NÃO MUDAR)

# Coordinates
CLICK_X, CLICK_Y = 62, 1020 # define onde vai clicar pra alterar (NÃO MUDAR)
VENDOR_X, VENDOR_Y = 272, 328 # define onde vai clicar pra botar o vendedor (NÃO MUDAR)
CONFIRMATION_X, CONFIRMATION_Y = 940, 877 # define onde vai clicar pra salvar (NÃO MUDAR)
VENDOR_NAME = "VINI" #define quem vai ser o vendedor, mudar se não quiser que seja o vinicius

# tempo de espera pra ir pra página
pyautogui.PAUSE = PAUSE_DURATION
time.sleep(3)

def initial_setup():
    """descer até o final e alinhar tudo."""
    pyautogui.scroll(INITIAL_SCROLL_DOWN)
    pyautogui.scroll(INITIAL_SCROLL_UP)

def click_coordinates(x, y):
    """Clicar nas coordenadas específicas e lidar com erros."""
    try:
        pyautogui.click(x, y)
    except pyautogui.FailSafeException:
        print("PyAutoGUI desligando.")
        exit()
    except pyautogui.PyAutoGUIException as e:
        print(f"PyAutoGUI deu erro quando foi clicar em: ({x}, {y}): {e}")
    except Exception as e:
        print(f"deu erro quando foi clicar em: ({x}, {y}): {e}")

def perform_vendor_action():
    """clicar no vendedor, escrever o nome e confirmar"""
    try:
        pyautogui.doubleClick(VENDOR_X, VENDOR_Y)
        pyautogui.write(VENDOR_NAME)
        time.sleep(0.4)
        pyautogui.press('enter')
        time.sleep(0.5)
        click_coordinates(CONFIRMATION_X, CONFIRMATION_Y)
    except pyautogui.PyAutoGUIException as e:
        print(f"PyAutoGUI deu erro no vendedor: {e}")
    except Exception as e:
        print(f"Erro no vendedor: {e}")

def scroll_up():
    """subir a tela depois de cada clcik"""
    pyautogui.scroll(SCROLL_UP_AMOUNT)

def realign_view():
    """realinhar a página depois de uma certa quantidade de clicks"""
    pyautogui.scroll(-REALIGN_SCROLL_UP)

def main():
    initial_setup()
    pieces_remaining = PIECE_COUNT
    clicks = 0
    click_y = CLICK_Y  

    while pieces_remaining > 0:
        click_coordinates(CLICK_X, click_y)
        perform_vendor_action()
        pieces_remaining -= 1
        clicks += 1

        # subir depois de cada click
        scroll_up()

        # realinhar a tela depois do limite de clicks
        if clicks >= MAX_CLICKS_BEFORE_REALIGN:
            realign_view()
            clicks = 0  # reiniciando o contador de clicks pra realinhar de novo depois

        # parte do final, que a páigna não sobe mais
        if pieces_remaining <= 19:
            click_y -= 45

    print("Feito.")

if __name__ == "__main__":
    main()