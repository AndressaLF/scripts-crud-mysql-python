import mysql.connector
from mysql.connector import Error  # para capturar exceção

print('Rotina para cadastro de Produtos no Banco de Dados -> db_produtos')

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

        print('Entre com os dados conforme solicitado')
        # solicitando dados do usuário

        while True:
            NomeProduto = str(input('Digite o nome do produto ou fim para sair:'))
            
            if NomeProduto == 'fim':
                break
            else:
                Preco = float(input('Digite o valor do produto separado por .:'))
                Quantidade = int(input('Digite a quantidade do produto:'))
                # declaração SQL a ser executada
                inserir_produtos = f"""INSERT INTO tb_produtos(NomeProduto, Preco, Quantidade) 
                                    VALUES ("{NomeProduto}",{Preco},{Quantidade})"""
               
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