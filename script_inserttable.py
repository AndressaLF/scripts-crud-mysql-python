import mysql.connector
from mysql.connector import Error  # para capturar exceção

try:
    # criando e inicializa a conexão
    conexao = mysql.connector.connect(
        host = 'localhost', 
        user = 'root', 
        password = 'admin', 
        database = 'db_backend',
        )

    # verifincando o sucesso da conexão utilizando as credenciais acima
    if conexao.is_connected():
        db_info = conexao.get_server_info()  # coletada dados da conexao
        print(f'Conexão realizada com sucesso ao servidor MySQL versão {db_info}!')

        # criar cursor e executar um comando dentro do banco
        cursor = conexao.cursor()
        cursor.execute("select database();")  # vai selecionar o banco de dados
        nome_bd = cursor.fetchone() # metodo fetchone, busca uma linha
        print("Conectado ao banco de dados", nome_bd)

        # declaração SQL a ser executada
        inserir_produtos = """INSERT INTO tb_produtos(NomeProduto, Preco, Quantidade) 
                            VALUES ('arroz', 8.00, 4),
                                    ('cuscuz', 3.00, 6),
                                    ('macarrao', 7.00, 3)
                                                 """
               
        # Executar SQL no banco de dados
        cursor.execute(inserir_produtos)  # vai executar o comando no banco de dados
        conexao.commit() #  tornar uma transação permanente/ grava no banco
        print(f'Foram inseridos um total de {cursor.rowcount} registros.')  # rowcount, propriedade do cursor

except Error as erro:
    print(f'Falha ao inserir dados no MySQL: {erro}')

# Desfazendo a conexão automaticamente:
finally:
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada!")