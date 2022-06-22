import mysql.connector
from mysql.connector import Error  # para capturar exceção
    
def conectar():
    try:
        global conexao, nome_bd
        # criando e inicializa a conexão
        conexao = mysql.connector.connect(
            host = 'localhost', 
            user = 'root', 
            password = 'admin', 
            database = 'db_backend',
            )

        # verifincando o sucesso da conexão utilizando as credenciais acima      
        cursor = conexao.is_connected()
        db_info = conexao.get_server_info()  # coletada dados da conexao
        print(f'Conexão realizada com sucesso ao servidor MySQL versão {db_info}!')

        # criar cursor e executar um comando dentro do banco
        cursor = conexao.cursor()
        cursor.execute("select database();")  # vai selecionar o banco de dados
        nome_bd = cursor.fetchone() # metodo fetchone, busca uma linha
        print("Conectado ao banco de dados", nome_bd)
    except Error as erro:
        print(f'Erro de conexão: {erro}')

# Criar consulta para ser realizada atraves do id
def consulta(IdProduto):
    try:
        cursor = conexao.cursor()
        consulta_sql = f'SELECT * FROM tb_produtos WHERE IdProduto = {IdProduto}'
        cursor.execute(consulta_sql)
        all_lines = cursor.fetchall()

        for line in all_lines:
            print(f"Id:{line[0]}")
            print(f"Produto: {line[1]}")
            print(f"Preço: {line[2]}")  
            print(f"Quantidade: {line[3]} \n") 
    except Error as erro:
        print(f'Falha ao consultar a tabela: {erro}')
    finally:
        if (conexao.is_connected()):
            cursor.close()
            conexao.close 

def atualiza(novo_preco, IdProduto):
    try:
        altera_preco = f"""UPDATE tb_produtos
                            SET Preco = {novo_preco}
                            WHERE IdProduto = {IdProduto}"""
    
        cursor = conexao.cursor()
        cursor.execute(altera_preco)
        conexao.commit()
        print('Preço alterado com sucesso!')
    except Error as erro:
        print(f'Falha ao consultar a tabela: {erro}')
    finally:
        if (conexao.is_connected()):
            cursor.close()
            conexao.close         


if __name__=='__main__':
    conectar() # estabelecer a conexao
    print('Atualizar preços de produto no banco de dados')
    print('Entre com os valores solicitados')
    IdProduto = int(input('Digite o Id do Produto que você deseja alterar:'))
    
    # passando o id para a função consulta
    consulta(IdProduto)

    novo_preco = float(input('Digite o novo preço para o produto selecionado:'))
    atualiza(novo_preco, IdProduto)

    verifica = input("\n Deseja consultar a atualização ? s ou n? ")
    if (verifica == 's'):
        consulta(IdProduto)
    print('\Até mais...')