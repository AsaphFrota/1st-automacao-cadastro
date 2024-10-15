
# Passo 1: Entrar no sistema da empresa - 
import pyautogui
import time
import pandas as pd

# VARIAVEIS
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pd.read_csv("produtos.csv")

pyautogui.PAUSE = 0.5

# abrir o navegador
## Apertar a tecla Win
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

# entrar no link - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login no sistema
pyautogui.hotkey("Ctrl", "t")
pyautogui.write(link)
pyautogui.press("enter")

# pausa de 5 segundos
time.sleep(4)

pyautogui.click(x=581, y=405)
pyautogui.write("asaphalves@hotmail.com")
# proximo campo de preenchimento
pyautogui.press("tab")
pyautogui.write("minhasenhaaqui")
#clicar no botao logar
pyautogui.click(x=680, y=564)

# Passo 3: Importar a base de dados
print(tabela)

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=565, y=292)
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preço
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #observação
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    #gravar
    pyautogui.press("enter")

    # Passo 5: Repetir o processo até acabar os produtos
    pyautogui.press("home")
