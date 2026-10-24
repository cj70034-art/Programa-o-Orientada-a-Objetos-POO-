
# Questão 1: Estoque de produtos

def exibir_menu():
    print("\n======== ESTOQUE DA LOJA =======")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir estoque")
    print("0 - Sair")
    print("================================")

def ler_quantidade(mensagem):
    """Lê um número inteiro maior ou igual a zero, repetindo a pergunta enquanto a entrada for inválida."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= 0:
                return valor
            else:
                print("Erro: A quantidade não pode ser negativa. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

def ler_nome(mensagem):
    """Lê um nome, removendo espaços e padronizando as iniciais (Title Case)."""
    while True:
        nome = input(mensagem).strip().title()
        if nome: # Verifica se não está vazio
            return nome
        print("Erro: O nome não pode ficar em branco.")

def adicionar_produto(estoque, nome, quantidade):
    """Insere o produto e indica se a operação foi realizada."""
    if nome in estoque:
        print(f"Erro: O produto '{nome}' já está cadastrado. Use a opção 3 para atualizar a quantidade.")
    else:
        estoque[nome] = quantidade
        print(f"Sucesso: Produto '{nome}' adicionado ao estoque com {quantidade} unidades.")

def remover_produto(estoque, nome):
    """Remove o produto e indica se a operação foi realizada."""
    if nome in estoque:
        del estoque[nome]
        print(f"Sucesso: Produto '{nome}' removido do estoque.")
    else:
        print(f"Erro: Produto '{nome}' não foi encontrado.")

def atualizar_quantidade(estoque, nome, quantidade):
    """Altera a quantidade e indica se a operação foi realizada."""
    if nome in estoque:
        estoque[nome] = quantidade
        print(f"Sucesso: Quantidade do produto '{nome}' atualizada para {quantidade}.")
    else:
        print(f"Erro: Produto '{nome}' não foi encontrado. Cadastre-o primeiro.")

def exibir_estoque(estoque):
    """Mostra todos os produtos e suas quantidades."""
    if not estoque: # Se o dicionário estiver vazio (equivale a len(estoque) == 0)
        print("Estoque vazio.")
        return
    
    print("\n--- PRODUTOS NO ESTOQUE ---")
    for nome, quantidade in estoque.items():
        print(f"- {nome}: {quantidade} unidades")
    print("---------------------------")

def main():
    # O dicionário que vai guardar os valores(chave: nome, valor: quantidade)
    estoque = {} 
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            nome = ler_nome("Nome do produto: ")
            quantidade = ler_quantidade("Quantidade inicial: ")
            adicionar_produto(estoque, nome, quantidade)
            
        elif opcao == "2":
            nome = ler_nome("Nome do produto a remover: ")
            remover_produto(estoque, nome)
            
        elif opcao == "3":
            nome = ler_nome("Nome do produto a atualizar: ")
            quantidade = ler_quantidade("Nova quantidade: ")
            atualizar_quantidade(estoque, nome, quantidade)
            
        elif opcao == "4":
            exibir_estoque(estoque)
            
        elif opcao == "0":
            print("Saindo do sistema... Até a próxima!")
            break
        else:
            print("Erro: Opção inválida. Digite um número de 0 a 4.")

# Inicia o programa
if __name__ == "__main__":
    main()