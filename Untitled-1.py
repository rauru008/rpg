from tkinter import *

turnos = 0
segundos = 0
minutos = 0
horas = 0
def tempos():
    global turnos, segundos
    turnos += 1
    segundos +=6
    minutos = segundos  / 60
    horas = minutos / 60
    texto3.config(text="Turnos: " + str(turnos))
    texto2.config(text="Segundos: " + str(segundos))
    texto4.config(text="Minutos: " + str(int(minutos)))
    texto5.config(text="Horas: " + str(int(horas)))

def subTempos():
    1 - turnos
    6 - turnos
    texto3.config(text="Turnos: " + str(turnos))
    texto2.config(text="Segundos: " + str(segundos))
    

janela = Tk()

janela.title("Janela")

janela.geometry("400x400")

texto = Label(janela, text="Contador de turnos e segundos")
texto.grid(column=0,row=0)

botao = Button(janela, text="Aperte para adicionar", command=tempos)
botao.grid(column=0,row=1)

botao2 = Button(janela, text="Aperte para diminiur", command=subTempos)
botao2.grid(column=1,row=1)

texto2 = Label(janela, text="Segundos: " + str(segundos))
texto2.grid(column=0,row=3)

texto3 = Label(janela, text="Turnos: " + str(turnos))
texto3.grid(column=0, row=2)

texto4 = Label(janela,text="Minutos: " + str(minutos))
texto4.grid(column=2,row=3)

texto5 = Label(janela,text="Horas: " + str(horas))
texto5.grid(column=5,row=3)
janela.mainloop()