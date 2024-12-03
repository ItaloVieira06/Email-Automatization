from send_email import *
from grid import*
from tkinter import *
from time import sleep

def enviar():
    enviar2()
    sleep(0.75)
    main.destroy()

#janela principal / main do projeto
main = Tk()
main.title("Enviador de API's")
main.geometry("400x400")

título = Label(main, text = "Clique abaixo para executar o código")
título.grid(column=0, row=0, padx=100, pady=100)


iniciar = Button(main, text="ENVIAR", command= enviar)
iniciar.grid(column=0, row=1, padx=100, pady=100)

main.mainloop()