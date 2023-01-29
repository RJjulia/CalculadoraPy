#criando e importando as bibliotecas
from tkinter import *
from tkinter import ttk

#criando e configurando uma janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x320")

#dividir a janela e continuar configurando
frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)

janela.mainloop()


