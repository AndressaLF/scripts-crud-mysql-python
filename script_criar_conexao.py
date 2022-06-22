import mysql.connector

# inicializa a conexão
conexao = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    password = 'admin', 
    database = 'dbplaylist1',  # nome do banco de dados
    )

# verificando o sucesso da conexão utilizando as credenciais acima
if conexao.is_connected():
    db_info = conexao.get_server_info()  # coletada dados da conexao
    print(f'Conexão realizada com sucesso ao servidor MySQL versão {db_info}!')

    # executando um comando dentro do banco
    cursor = conexao.cursor()
    cursor.execute("select database();")  # vai selecionar o nome do banco de dados
    nome_bd = cursor.fetchone() # metodo fetchone, busca uma linha
    print("Conectado ao banco de dados", nome_bd)
else:
    print('Erro - Conexão não realizada')

# Desfazendo a conexão automaticamente:
if conexao.is_connected():
    cursor.close()
    conexao.close()
    print("Conexão encerrada!")