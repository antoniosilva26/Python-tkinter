from tkinter import * 
import tkinter as tk

janela = tk.Tk()


class Configs():
    def __init__(self):
        self.janela = janela
        janela.title("Cadastro")
        janela.geometry("300x300")
        janela.resizable(True, True)
        label2 = tk.Frame(janela, bg='lightblue', bd=1, relief='sunken')
        label2.pack(padx=20, pady=20, fill='both', expand=True)
        label = tk.Label(label2, text="Cadastro!", bg="lightblue", font='Arial 12').pack()
        label3 = tk.Label(label2, text="Nome", bg="lightblue", font='Arial 12').pack(pady=5)
        entry_nome = tk.Entry(label2, width=30, show='*').pack(pady=10)
        label4 = tk.Label(label2, text="Senha", bg="lightblue", font='Arial 12').pack(pady=5)
        entry_senha = tk.Entry(label2, width=30, show='*').pack(pady=10)
        BotaoCadastro = Button(label2, text="Cadastro")
        BotaoCancelar = Button(label2, text="Cancelar")
        BotaoCadastro.place(y=180, x=102)
        BotaoCancelar.place(y=210, x=102)
class Aplication():
    def __init__(self):
        self.janela = janela
        Configs()
        janela.mainloop()
Aplication()

