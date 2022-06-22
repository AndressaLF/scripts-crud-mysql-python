import mysql.connector

try:
    # criando e inicializa a conexão
    conexao = mysql.connector.connect(
        host = 'localhost', 
        user = 'root', 
        password = 'admin', 
        database = 'db_backend', # banco de dados já criado
        )

    # verificando o sucesso da conexão utilizando as credenciais acima
    if conexao.is_connected():
        db_info = conexao.get_server_info()  # coletada dados da conexao
        print(f'Conexão realizada com sucesso ao servidor MySQL versão {db_info}!')

        # criar cursor e executar um comando dentro do banco
        cursor = conexao.cursor()
        cursor.execute("select database();")  # vai selecionar o banco de dados
        nome_bd = cursor.fetchone() # metodo fetchone, busca uma linha
        print("Conectado ao banco de dados", nome_bd)

        # declaração SQL a ser executada
        criar_tabela_SQL = """CREATE TABLE tb_Produtos (
                                IdProduto tinyint(4) NOT NULL AUTO_INCREMENT,
                                NomeProduto varchar(40) NOT NULL,
                                Preco float NOT NULL,
                                Quantidade tinyint(4) NOT NULL,
                                PRIMARY KEY (IdProduto))"""
        
        # Executar SQL no banco de dados
        cursor.execute(criar_tabela_SQL)  # vai executar o comando no banco de dados
        print('Tabela de Produtos criada com sucesso!')
        
except mysql.connector.Error as erro:
    print(f'Falha ao criar a tabela no MySQL: {erro}')

# Desfazendo a conexão automaticamente:
finally:
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada!")