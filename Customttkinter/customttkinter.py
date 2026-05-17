from customtkinter import *

app = CTk()
app.geometry("700x600")


set_appearance_mode("dark")

# Sistema de registro

class Princpal():
    def __init__(self):
        self.app = app
        self.frameprincipal = CTkFrame(master=app, border_width=2, corner_radius=20, width=600, height=500)
        self.frameprincipal.pack_propagate(False)
        self.frameprincipal.pack(expand=True)
        self.textocadastro = CTkLabel(master=self.frameprincipal, text="Cadastro")
        self.textocadastro.pack(pady=10)

        self.nomeentry = CTkEntry(master=self.frameprincipal, placeholder_text="Digite seu nome")
        self.nomeentry.pack(pady = 10, padx = 20)

        self.senhaentry = CTkEntry(master=self.frameprincipal, placeholder_text="Digite sua senha")
        self.senhaentry.pack(pady = 10, padx = 20)

        self.emailentry = CTkEntry(master=self.frameprincipal, placeholder_text="Digite seu email")
        self.emailentry.pack(pady = 10, padx = 20)

        self.cpfentry = CTkEntry(master=self.frameprincipal, placeholder_text="Digite seu CPF")
        self.cpfentry.pack(pady = 10, padx = 20)

        self.generocaixa = CTkComboBox(master=self.frameprincipal, values=["Masculino", "Feminino", "Prefiro não Dizer"])
        self.generocaixa.pack(pady = 10)

        self.erro_label = CTkLabel(master=self.frameprincipal, text="")
        self.erro_label.pack(pady=5)

        btn = CTkButton(master = self.frameprincipal, text="Cadastrar", corner_radius=20, border_width=2, command=self.ClicouConfirmar) 
        btn.pack(pady=20)


        btn2 = CTkButton(master = self.frameprincipal, text="Cancelar", corner_radius=20, border_width=2, command=self.FecharDesktop) 
        btn2.pack(pady=20)       
    def FecharCadastro(self):
        app.destroy()
    def FecharDesktop(self):
        self.frameprincipal.destroy()
    def ClicouConfirmar(self):

        nome = self.nomeentry.get()
        senha = self.senhaentry.get()
        email = self.emailentry.get()
        cpf = self.cpfentry.get()
        genero = self.generocaixa.get()

        if nome == "" or senha == "" or email == "" or cpf == "":
            self.textocadastro.configure(
                text="Preencha todos os formulários!"
            )
            return

        self.erro_label.configure(text="")

        frameprincipal = CTkFrame(
            master=app,
            border_width=2,
            corner_radius=20,
            width=600,
            height=500
        )

        frameprincipal.pack_propagate(True)
        frameprincipal.pack(expand=True)

        texto = CTkLabel(
            master=frameprincipal,
            text=f"Obrigado, seu registro foi concluído com sucesso!\n\nSeu Nome cadastrado: {nome}\n\nSua Senha cadastrada: {senha}\n\nSeu Email cadastrado: {email}\n\nSeu CPF cadastrado: {cpf}\n\nSeu Gênero registrado: {genero}"
        )

        texto.pack(pady=10, padx=10)

        botaofechar = CTkButton(
            master=frameprincipal,
            text="Fechar",
            corner_radius=20,
            border_width=2,
            command=self.FecharCadastro
        )

        botaofechar.pack(pady=20)

        self.frameprincipal.destroy()

Princpal()
app.mainloop()
