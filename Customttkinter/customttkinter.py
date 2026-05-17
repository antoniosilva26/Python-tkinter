from customtkinter import *

app = CTk()
app.geometry("700x600")

set_appearance_mode("dark")

# Sistema de registro

class Configs():
    def __init__(self):
        self.app = app
        frameprincipal = CTkFrame(master=app, border_width=2, corner_radius=20, width=600, height=500)
        frameprincipal.pack_propagate(False)
        frameprincipal.pack(expand=True)
        textocadastro = CTkLabel(master=frameprincipal, text="Cadastro").pack(pady=10)

        nomeentry = CTkEntry(master=frameprincipal, placeholder_text="Digite seu nome")
        nomeentry.pack(pady = 10, padx = 20)

        nomeentry = CTkEntry(master=frameprincipal, placeholder_text="Digite sua senha")
        nomeentry.pack(pady = 10, padx = 20)

        nomeentry = CTkEntry(master=frameprincipal, placeholder_text="Digite seu email")
        nomeentry.pack(pady = 10, padx = 20)

        cpfentry = CTkEntry(master=frameprincipal, placeholder_text="Digite seu CPF")
        cpfentry.pack(pady = 10, padx = 20)

        generocaixa = CTkComboBox(master=frameprincipal, values=["Masculino", "Feminino", "Prefiro não Dizer"])
        generocaixa.pack(pady = 10)

        btn = CTkButton(master = frameprincipal, text="Cadastrar", corner_radius=20, border_width=2) 
        btn.pack(pady=20)

        btn2 = CTkButton(master = frameprincipal, text="Cancelar", corner_radius=20, border_width=2) 
        btn2.pack(pady=20)

Configs()
app.mainloop()