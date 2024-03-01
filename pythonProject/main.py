import requests
import tkinter
from tkinter import *
from tkinter import Tk,StringVar,ttk
from tkinter import messagebox
from sql import *

#EncerrarComando
#cor
cor01="#F0FFFF"
cor02="#FFFFFF"
cor03="#FF0000"
cor04="#000000"
cor05="#6d706e"

#Comando para criar a janela
janela=Tk()
#titulo da tela
janela.title("Auto Peças BD")
#Tamanho da tela
janela.geometry('900x600')
janela.resizable(width=False,height=False)
#Formatação de cor
janela.configure(background=cor02)
style=ttk.Style(janela)
style.theme_use("clam")

#criando frame
frameCima=Frame(janela,width=1043,height=50,bg=cor01,relief=FLAT)
frameCima.grid(row=0,column=0,)

frameMeio=Frame(janela,width=1043,height=303,bg=cor01,relief=FLAT)
frameMeio.grid(row=1,column=0,pady=1,padx=0,stick=NSEW)

frameBaixo = Frame(janela,width=1043,height=300,relief=FLAT)
frameBaixo.grid(row=2,column=0,pady=0,padx=1,stick=NSEW)
#Funçoes
global tree


#Funçoes para inserir informação
# Função para realizar a pesquisa no banco de dados
def pesquisar():
    # Obtenha os valores inseridos pelo usuário
    codigo_produto = et_Codproduto.get()
    nome_produto = et_NomeProduto.get()
    cod_fornecedor = et_Cod_Fornecedor.get()
    cod_loja = et_Loja_Cod_Loja.get()

    # Construa a consulta SQL com base nos valores inseridos
    # (Isso é um exemplo, você precisa adaptar para a estrutura do seu banco de dados)
    query = "SELECT * FROM produto WHERE Cod_Produto = %s AND Nome_Produto = %s AND Fornecedor = %s AND Loja_Cod_Loja = %s"

    # Execute a consulta no banco de dados
    cur.execute(query, (codigo_produto, nome_produto, cod_fornecedor, cod_loja))

    # Obtenha os resultados da consulta
    resultados = cur.fetchall()

    # Limpe a exibição anterior na Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Preencha a Treeview com os resultados
    for resultado in resultados:
        tree.insert('', 'end', values=resultado)
#Frame de Titulo
app_logo=Label(frameCima,text='Auto Peças BD',width=900,compound=LEFT,relief=RAISED,anchor=NW,font=('Verdana 25 bold'),bg=cor02,fg=cor05)
app_logo.place(x=0,y=0)

#Trabalhando no frema Meio
lb_Codproduto=Label(frameMeio,text='Codigo do Produto: ',height=1,anchor=NW,font=('ivy 10 bold'),bg=cor01,fg=cor04)
lb_Codproduto.place(x=15, y=10)
et_Codproduto = Entry(frameMeio, width=30, justify='left',relief=SOLID)
et_Codproduto.place(x=150, y=11)

lb_NomeProduto=Label(frameMeio,text='Nome do Produto: ',height=1,anchor=NW,font=('ivy 10 bold'),bg=cor01,fg=cor04)
lb_NomeProduto.place(x=15, y=50)
et_NomeProduto = Entry(frameMeio, width=30, justify='left',relief=SOLID)
et_NomeProduto.place(x=150, y=51)

#lb_Descricao=Label(frameMeio,text='Descrição: ',height=1,anchor=NW,font=('ivy 10 bold'),bg=cor01,fg=cor04)
#lb_Descricao.place(x=15, y=70)
#et_Descricao = Entry(frameMeio, width=30, justify='left',relief=SOLID)
#et_Descricao.place(x=150, y=71)

lb_Cod_Fornecedor=Label(frameMeio,text='Cód do Fornecedor: ',height=1,anchor=NW,font=('ivy 10 bold'),bg=cor01,fg=cor04)
lb_Cod_Fornecedor.place(x=15, y=90)
et_Cod_Fornecedor = Entry(frameMeio, width=30, justify='left',relief=SOLID)
et_Cod_Fornecedor.place(x=150, y=91)

#lb_QTD_Estoque=Label(frameMeio,text='QTD Estoque: ',height=1,anchor=NW,font=('ivy 10 bold'),bg=cor01,fg=cor04)
#lb_QTD_Estoque.place(x=15, y=130)
#et_QTD_Estoque = Entry(frameMeio, width=30, justify='left',relief=SOLID)
#et_QTD_Estoque.place(x=150, y=131)

#lb_Locacao=Label(frameMeio,text='Posição do Produto: ',height=1,anchor=NW,font=('ivy 10 bold'),bg=cor01,fg=cor04)
#lb_Locacao.place(x=15, y=160)
#et_Locacao = Entry(frameMeio, width=30, justify='left',relief=SOLID)
#et_Locacao.place(x=150, y=161)

lb_Loja_Cod_Loja=Label(frameMeio,text='Loja: ',height=1,anchor=NW,font=('ivy 10 bold'),bg=cor01,fg=cor04)
lb_Loja_Cod_Loja.place(x=15, y=130)
et_Loja_Cod_Loja = Entry(frameMeio, width=30, justify='left',relief=SOLID)
et_Loja_Cod_Loja.place(x=150, y=131)

#Valor do produto

#lb_Tolal=Label(frameMeio,text='',width=14,height=2,anchor=CENTER,font=('ivy 15 bold'),bg=cor02,fg=cor04)
#lb_Tolal.place(x=370, y=10)
#lb_Tolal=Label(frameMeio,text='Valor Produto ',height=1,anchor=NW,font=('ivy 10 bold'),bg=cor02,fg=cor04)
#lb_Tolal.place(x=400, y=12)

#Labels Quantidade
#lb_Qtd=Label(frameMeio,text='',width=14,height=2,anchor=CENTER,font=('ivy 15 bold'),bg=cor02,fg=cor04)
#lb_Qtd.place(x=370, y=70)
#lb_Qtd=Label(frameMeio,text='Qtd Estoque ',height=1,anchor=NW,font=('ivy 10 bold'),bg=cor02,fg=cor04)
#lb_Qtd.place(x=415, y=72)
#criar botao

lb_Pesquisa=Button(frameMeio,command=pesquisar,width=20,text='Pesquisar'.upper(),compound=CENTER,anchor=CENTER,font=('ivy 10 bold'),bg=cor02,fg=cor04)
lb_Pesquisa.place(x=100, y=180)

#tabela Lista em baixo
def mostrar():

    Tabela_head=['Cod Produto','Nome Produto','Descrição','Fornecedor','Qtd Estoque','Localização','Loja']
    #botao=Button(janela,text='Buscar Selecione',command= mostrar)
    #botao.grid(column=1,row=1)
    lista_intens=ver_forma()
    tree=ttk.Treeview(frameBaixo,selectmode="extended",columns=Tabela_head,show="headings")

    #vertical scrollbar
    V_sb=ttk.Scrollbar(frameBaixo,orient="vertical",command=tree.yview)

    #horizontal scrollbar
    H_sb=ttk.Scrollbar(frameBaixo,orient="horizontal",command=tree.xview)

    tree.configure(yscrollcommand=V_sb.set,xscrollcommand=H_sb.set)
    tree.grid(column=0, row=0, stick='nsew')
    V_sb.grid(column=1, row=0, stick='ns')
    H_sb.grid(column=0, row=1, stick='ew')
    frameBaixo.grid_rowconfigure(0,weight=12)

    hd=['center','center','center','center','center','center','center']
    h=[100,140,180,160,100,100,100]
    n=0

    for col in Tabela_head:
        tree.heading(col,text=col.title(),anchor=CENTER)
        #adjust the coluns
        tree.column(col,width=h[n],anchor=hd[n])
        n+=1

    for item in lista_intens:
        tree.insert('','end',values=item)



mostrar()
   # quantidade=[]

   # for iten in lista_intens:
    #    quantidade.append(iten[7])

   # Total_valor=sum(quantidade)
  #  Total_itens=len(quantidade)

   # lb_Tolal['text']='R${:,.2f}'.format(Total_valor)
  #  lb_Qtd['text']=Total_itens


#Comando para manter a tela aberta
janela.mainloop()
cur.close()
conexao.close()
