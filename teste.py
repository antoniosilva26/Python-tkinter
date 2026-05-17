from tkinter import * 
import tkinter as tk
from tkinter import messagebox
import time

janela = tk.Tk()

nome = "_"
    

class Configs():
    def __init__(self):
        self.janela = janela
        janela.title("Cadastro")
        janela.geometry("500x500")
        janela.resizable(True, True)
        label2 = tk.Frame(janela, bg='lightblue', bd=1, relief='sunken')
        label2.pack(padx=20, pady=20, fill='both', expand=True)
        labelTitulo = tk.Label(label2, text="Cadastro", bg="lightblue", font='Arial 12', ).pack()
        labelNome = tk.Label(label2, text="Nome", bg="lightblue", font='Arial 12').pack(pady=5)
        self.entry_nome = tk.Entry(label2, width=30)
        self.entry_nome.pack(pady=10)
        labelSenha = tk.Label(label2, text="Senha", bg="lightblue", font='Arial 12').pack(pady=5)
        self.entry_senha = tk.Entry(label2, width=30, show='*')
        self.entry_senha.pack(pady=10)
        labelEmail = tk.Label(label2, text="Email", bg="lightblue", font='Arial 12').pack(pady=5)
        self.entry_email = tk.Entry(label2, width=30, show='*')
        self.entry_email.pack(pady=10)
        labelTelefone = tk.Label(label2, text="Telefone", bg="lightblue", font='Arial 12').pack(pady=5)
        self.entry_telefone = tk.Entry(label2, width=30, show='*')
        self.entry_telefone.pack(pady=10)
        BotaoCadastro = Button(label2, text="Cadastro", font='Arial 12', width=15, command=self.Cadastro)
        BotaoCancelar = Button(label2, text="Cancelar", font='Arial 12', width=15, command=self.Cancelou)
        BotaoCadastro.place(y=340, x=157)
        BotaoCancelar.place(y=390, x=157)
    def Cadastro(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()
        msgnome = messagebox.showinfo("Cadastro", f"Cadastro concluido com sucesso, {nome}! \n Sua senha é: {senha}")
    def Cancelou(self):
        janela.destroy()
        

    #janela.destroy()
class Aplication():
    def __init__(self):
        self.janela = janela
        Configs()
        janela.mainloop()
Aplication()

