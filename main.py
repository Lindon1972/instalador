from tkinter import filedialog, messagebox
import os, shutil

messagebox.showinfo("Instalação SIGEP", "Escolha uma pasta pública para instalar o banco!")
destino = filedialog.askdirectory()

os.makedirs(os.path.join(destino, "SIGEP"))
os.makedirs(os.path.join(destino, "SIGEP", "pdfs"))
os.makedirs(os.path.join(destino, "SIGEP", "banco"))
os.makedirs(os.path.join(destino, "SIGEP", "icones"))

mensagem = "Pastas criadas com sucesso!\n"
mensagem = mensagem + "Agora vá na pasta DOWNLOADS e\n"
mensagem = mensagem + "Clique duas vezes na pasta banco_SIGEP.\n"
mensagem = mensagem + "Depois clique em OK."

messagebox.showinfo("Instalação SIGEP", mensagem)

destinoI = os.path.join(destino, "SIGEP")
origem = filedialog.askdirectory()

shutil.copytree(origem, destinoI, dirs_exist_ok=True)

mensagem = "Banco copiado com sucesso!\n"
mensagem = mensagem + "Agora escolha uma pasta no seu login.\n"
mensagem = mensagem + "Clique nela duas vezes para selecioná-la.\n"
mensagem = mensagem + "Depois em OK para concluir."
messagebox.showinfo("Instalação SIGEP", mensagem)

app = filedialog.askdirectory()
os.makedirs(os.path.join(app, "app_SIGEP"))

mensagem = "Para finalizar:\n"
mensagem = mensagem + "Vá na pasta DOWNLOADS e\n"
mensagem = mensagem + "Clique duas vezes na pasta app_SIGEP.\n"
mensagem = mensagem + "Depois clique em OK."
messagebox.showinfo("Instalação SIGEP", mensagem)

origem = filedialog.askdirectory()
destinoI = os.path.join(app, "app_SIGEP")

shutil.copytree(origem, destinoI, dirs_exist_ok=True)

mensagem = "Instalação concluida com sucesso!\n"
mensagem = mensagem + "Vá na pasta app_SIGEP e\n"
mensagem = mensagem + "Clique com o botão direito do mouse no aplicativo.\n"
mensagem = mensagem + "Dentre as opções escolha a que envia para área de trabalho e cria um ATALHO."
messagebox.showinfo("Instalação SIGEP", mensagem)