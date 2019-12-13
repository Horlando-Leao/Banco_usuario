from tkinter import *
from conversor import *

def Janela_Menu_principal():
    
    janela_menu = Tk()
    janela_menu.geometry('600x600')
    janela_menu.title('MENU do Gerenciador ')
    janela_menu.configure()

    rotulo1 = Label(janela_menu, text="____________________________MENU____________________________", font= 'Helvetic', bg = 'blue').pack(side=TOP)

    botao1 = Button(janela_menu, width=20, text='Cadastrar cliente', 
    command = Janela_cadastro_usuario)
    botao1.place(x=100, y=120)

    botao2 = Button(janela_menu, width=20, text='Consultar cliente', 
    command = Janela_consulta_usuario)
    botao2.place(x=100, y=150)

    botao3 = Button(janela_menu, width=20, text='Atualizar cadastro', 
    command = Janela_atualizacao_usuario)
    botao3.place(x=100, y=180)

    botao4 = Button(janela_menu, width=20, text='Excluir Cadastro', 
    command = Janela_exclusao_usuario)
    botao4.place(x=100, y=210)

    janela_menu.mainloop()
    
def Janela_cadastro_usuario():
    #configuração janela
    
    janela_1 = Tk()
    janela_1.geometry('600x600')
    janela_1.title('Cadastro de Cliente ')
    janela_1.configure()
    

    botao2 = Button(janela_1, width=7, text='MENU', 
    command = Janela_Menu_principal)
    botao2.place(x=20, y=20)

    rotulo1 = Label(janela_1, text="Inseria os seguintes dados(em minisculo)", font= "Arial 14")
    rotulo1.place(x=70, y=65)

    rotulo2 = Label(janela_1, text="Nome completo: ")
    rotulo2.place(x=70, y=100)

    caixa1 = Entry(janela_1)
    caixa1.place(x=176, y=100, width=200)

    rotulo3 = Label(janela_1, text="Telefone: ")
    rotulo3.place(x=70, y=125)

    caixa2 = Entry(janela_1)
    caixa2.place(x=176, y=125, width=200)

    rotulo4 = Label(janela_1, text="E-mail: ")
    rotulo4.place(x=70, y=150)

    caixa3 = Entry(janela_1)
    caixa3.place(x=176, y=150, width=200)
            
    botao1 = Button(janela_1, width=21, text='Cadastrar', 
    command = lambda: Converter_enviar_para_dml_inserir_usuario(caixa1.get(), caixa2.get(), caixa3.get()))
    botao1.place(x=176, y=180)
    
    janela_1.mainloop()  

def Janela_consulta_usuario():

    janela_1 = Tk()
    janela_1.geometry('600x600')
    janela_1.title('Consulta de Clientes')

    botao2 = Button(janela_1, width=7, text='MENU', bg = '#5882FA', 
    command = Janela_Menu_principal )
    botao2.place(x=20, y=20)
    
    rotulo1 = Label(janela_1, text="Inseria os seguintes dados(em minisculo)", font= 150).pack(side=TOP)

    rotulo2 = Label(janela_1, text="Pesquisar por...: ")
    rotulo2.place(x=55, y=100)

    caixa1 = Entry(janela_1)
    caixa1.place(x=176, y=100, width=200)

    rotulo3 = Label(janela_1, text="Digite: ")
    rotulo3.place(x=135, y=125)

    caixa2 = Entry(janela_1)
    caixa2.place(x=176, y=125, width=200)

    botao1 = Button(janela_1, width=21, text='Consultar', 
    command = lambda: Converter_enviar_para_dml_pesquisar_usuario(caixa2.get(), caixa1.get()))
    botao1.place(x=176, y=180)

    janela_1.mainloop()

def Janela_atualizacao_usuario():
    janela_1 = Tk()
    janela_1.geometry('600x600')
    janela_1.title('Atualizar Cadastro de Clientes')

    rotulo1 = Label(janela_1, text="Inseria os seguintes dados(em minisculo)", font= 150).pack(side=TOP)

    rotulo2 = Label(janela_1, text="Insira o nome para mudar e o E-mail para validação", font= 'Arial').pack(side=BOTTOM)

    botao2 = Button(janela_1, width=7, text='MENU', bg = '#5882FA', 
    command = Janela_Menu_principal )
    botao2.place(x=20, y=20)
    
    rotulo3 = Label(janela_1, text="Nome completo: ")
    rotulo3.place(x=75, y=100)

    caixa1 = Entry(janela_1)
    caixa1.place(x=176, y=100, width=200)

    rotulo4 = Label(janela_1, text="E-mail: ")
    rotulo4.place(x=133, y=125)

    caixa2 = Entry(janela_1)
    caixa2.place(x=176, y=125, width=200)

    botao1 = Button(janela_1, width=21, text='Atualizar', 
    command = lambda: Converter_enviar_para_atualizar_usuario(caixa1.get(),caixa2.get()))
    botao1.place(x=176, y=180)

    janela_1.mainloop()

def Janela_exclusao_usuario():
    janela_1 = Tk()
    janela_1.geometry('600x600')
    janela_1.title('Exclusão de Clientes')

    botao2 = Button(janela_1, width=7, text='MENU', bg = '#5882FA', 
    command = Janela_Menu_principal )
    botao2.place(x=20, y=20)
    
    rotulo1 = Label(janela_1, text="Inseria os seguintes dados(em minisculo)", font= 150).pack(side=TOP)

    rotulo2 = Label(janela_1, text="Atenção todos os dados dos clientes serão removidos", font= 'Arial').pack(side=BOTTOM)

    rotulo3 = Label(janela_1, text="E-mail: ")
    rotulo3.place(x=133, y=100)

    caixa1 = Entry(janela_1)
    caixa1.place(x=176, y=100, width=200)

    botao1 = Button(janela_1, width=21, text='Excluir',
    command = lambda: Converter_enviar_para_dml_excluir_usuario(caixa1.get()))
    botao1.place(x=176, y=180)

    janela_1.mainloop()

Janela_Menu_principal()

'''command, compound, default, height,
overrelief, state, width'''
