from tkinter import * 

janela = Tk()


class Configs():
    def __init__(self):
        self.janela = janela
        janela.title("Cadastro")
        janela.geometry("500x500")
        janela.resizable(True, True)
        BotaoCadastro = Button( text="Cadastro")
        BotaoCancelar = Button( text="Cancelar")
        BotaoCadastro.place(x=210, y=300)
        BotaoCancelar.place(x=210, y=350)
        text = Text(janela)
        text.insert(INSERT, "Eae")
        text.pack()

class Aplication():
    def __init__(self):
        self.janela = janela
        Configs()
        janela.mainloop()
Aplication()

