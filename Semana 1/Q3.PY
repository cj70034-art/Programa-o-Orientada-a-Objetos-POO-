# Questão 3: Controle de tarefas

def exibir_menu():
    print("\n====== CONTROLE DE TAREFAS ======")
    print("1 - Adicionar tarefa")
    print("2 - Marcar tarefa como concluída")
    print("3 - Listar tarefas")
    print("0 - Sair")
    print("=================================")

def ler_texto(mensagem):
    """Lê um texto e repete a pergunta enquanto ele estiver vazio."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Erro: Este campo não pode ficar em branco. Tente novamente.")

def buscar_tarefa(tarefas, titulo):
    """Percorre a lista e devolve o dicionário da tarefa encontrada, ou None se não existir."""
    for tarefa in tarefas:
        if tarefa["titulo"].lower() == titulo.lower():
            return tarefa
    return None

def adicionar_tarefa(tarefas, titulo, descricao):
    """Cria o dicionário da tarefa, acrescenta à lista e indica se a operação foi realizada."""
    if buscar_tarefa(tarefas, titulo) is not None:
        print(f"Erro: Já existe uma tarefa com o título '{titulo}'. Tente outro título.")
        return

    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente" # Toda tarefa nova começa como Pendente
    }
    tarefas.append(nova_tarefa)
    print(f"Sucesso: Tarefa '{titulo}' adicionada!")

def concluir_tarefa(tarefas, titulo):
    """Altera o status da tarefa para 'Concluído' e indica se a operação foi realizada."""
    tarefa = buscar_tarefa(tarefas, titulo)
    
    if tarefa is None:
        print(f"Erro: Tarefa '{titulo}' não foi encontrada.")
    elif tarefa["status"] == "Concluído":
        print(f"Aviso: A tarefa '{titulo}' já estava concluída.")
    else:
        tarefa["status"] = "Concluído"
        print(f"Sucesso: Tarefa '{titulo}' marcada como concluída!")

def listar_tarefas(tarefas):
    """Mostra as tarefas em duas seções, pendentes e concluídas."""
    # Separando as tarefas usando list comprehension
    pendentes = [t for t in tarefas if t["status"] == "Pendente"]
    concluidas = [t for t in tarefas if t["status"] == "Concluído"]
    
    # Seção de Pendentes
    print(f"\n--- PENDENTES ({len(pendentes)}) ---")
    if not pendentes:
        print("Nenhuma tarefa")
    else:
        # enumerate(..., start=1) cria a numeração 1, 2, 3...
        for i, tarefa in enumerate(pendentes, start=1):
            print(f"{i}. {tarefa['titulo']}: {tarefa['descricao']}")
            
    # Seção de Concluídas
    print(f"\n--- CONCLUÍDAS ({len(concluidas)}) ---")
    if not concluidas:
        print("Nenhuma tarefa")
    else:
        for i, tarefa in enumerate(concluidas, start=1):
            print(f"{i}. {tarefa['titulo']}: {tarefa['descricao']}")

def main():
    # banco de dados vai inicializar com a lista vazia
    tarefas = []
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            titulo = ler_texto("Título da tarefa: ")
            descricao = ler_texto("Descrição da tarefa: ")
            adicionar_tarefa(tarefas, titulo, descricao)
            
        elif opcao == "2":
            titulo = ler_texto("Título da tarefa a concluir: ")
            concluir_tarefa(tarefas, titulo)
            
        elif opcao == "3":
            if not tarefas: # Se a lista geral estiver vazia
                print("Nenhuma tarefa cadastrada no sistema.")
            else:
                listar_tarefas(tarefas)
                
        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Erro: Opção inválida. Digite um número de 0 a 3.")

if __name__ == "__main__":
    main()