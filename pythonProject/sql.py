import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='01020304',
    database='autopecasbd',
)
cur = conexao.cursor()
# CRUD

# Read
def inserir_form(i):
    with conexao:
        cur = conexao.cursor()
        comando_sql='INSERT INTO produto (Cod_Produto,Nome_Produto,Descrição,Fornecedor,QTD_Estoque,Locacao,Loja_Cod_Loja) values (?,?,?,?,?,?,?);'
        cur.execute(comando_sql,i)
        conexao.commit()#gravar no banco
#ver todos os dados
def ver_forma():
    ler_dados=[]
    with conexao:
        cur=conexao.cursor()
        comando_sql="select * from produto;"
        cur.execute(comando_sql)
        #resultado=cursor.fetchall()#ler o banco de dados
        #ler_dados=[]=resultado
        rows=cur.fetchall()
        for row in rows:
            ler_dados.append(row)
    return ler_dados



#ver todos os dados
def ver_item():
    ler_dados_individual = []
    with conexao:
        cur = conexao.cursor()
        query = "SELECT * FROM sua_tabela WHERE codigo_produto = %s AND nome_produto = %s AND cod_fornecedor = %s AND cod_loja = %s"
        cur.execute(query,(codigo_produto, nome_produto, cod_fornecedor, cod_loja))
        rows = cur.fetchall()
        for row in rows:
            ler_dados_individual.append(row)
    return ler_dados_individual




'''
def listar_select():
    comando_sql=f'select {} from produto;'
    cursor.execute(comando_sql)
    resultado=cursor.fetchall()#ler o banco de dados
    lista_intens=[]=resultado

elif selec == 'u':
    #Update
    posicao=input('Escolha a posição para ser Alterada:')
    Nome=input('Digite o nome:')
    comando_sql=f'UPDATE tabpai SET Nome_Pai="{Nome}" WHERE Cod_pai = {posicao};'
    cursor.execute(comando_sql)
    conexao.commit()#gravar no banco

elif selec == 'd':
    #Delete
    posicao=input('Delete da tabela a posição :')
    comando_sql=f'DELETE FROM tabpai WHERE Cod_pai = {posicao};'
    cursor.execute(comando_sql)
    conexao.commit()#gravar no banco
'''
