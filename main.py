#criando e importando as bibliotecas
from tkinter import *
from tkinter import ttk

#criando as cores
cor1 = "a1e1h1e" #preto
cor2 = "87CEEB"  #azul
cor3 = "#ECEFF!"  #cinza
cor4 = "FF1493"  #rosa
cor5 = "FFFAFA"  #snow

#criando e configurando uma janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x320")
janela.config(bg=cor1)

#dividir a janela e continuar configurando
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_body = Frame(janela, width=235, height=268)
frame_body.grid(row=1, column=0)

#criando os botoes
b1 = Button(frame_body, text="C", width=11, height=2, bg=cor3, font=('Ivy 13q bold'), relief=RAISED)
b1.place(x=0, y=0)

b2 = Button(frame_body, text="%", width=5, height=2, bg=cor3)
b2.place(x=90, y=0)

b3 = Button(frame_body, text="%", width=5, height=2, bg=cor4,fg=cor5)
b3.place(x=177, y=0)

janela.mainloop()


