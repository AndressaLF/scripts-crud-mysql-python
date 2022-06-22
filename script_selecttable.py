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
        consulta_sql = "select * from tb_produtos"
               
        # Executar SQL no banco de dados
        cursor.execute(consulta_sql)  # vai executar o comando no banco de dados
        all_lines = cursor.fetchall()
        print('Número total de registros retornados:', cursor.rowcount)

        print("\n Mostrando os Produtos cadastrados")
        for line in all_lines:
            print(f"Id:{line[0]}")
            print(f"Produto: {line[1]}")
            print(f"Preço: {line[2]}")  
            print(f"Quantidade: {line[3]} \n")  
        #print(all_lines)  # vetor de colunas
except Error as erro:
    print(f'Falha ao acessar a tabela no MySQL: {erro}')

# Desfazendo a conexão automaticamente:
finally:
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada!")