#criando e importando as bibliotecas
from tkinter import *
from tkinter import ttk

#criando as cores
cor1 = "a1e1h1e" #preto
cor2 = "87CEEB"  #azul
cor3 = "8A2BE2"  #roxo
cor4 = "FF1493"  #rosa
cor5 = "FFFAFA"  #snow

#criando e configurando uma janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x320")
janela.config(bg=cor1)

#dividir a janela e continuar configurando
frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)

frame_body = Frame(janela, width=235, height=268)
frame_body.grid(row=1, column=0)

janela.mainloop()


