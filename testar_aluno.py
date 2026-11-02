from aluno import Aluno

# 1. Lendo alunos em laço
lista_alunos = []

print("Cadastro de alunos (deixe o nome vazio para sair):")
while True:
    nome = input("Nome: ").strip()
    if not nome:
        break
    matricula = input("Matrícula: ").strip()
    
    novo_aluno = Aluno(nome, matricula)
    lista_alunos.append(novo_aluno)

# 2. Atribuindo notas e faltas diretamente
# Vamos fingir que cadastramos pelo menos 3 alunos para o teste:
if len(lista_alunos) >= 3:
    lista_alunos[0].notas.append(8.5)
    lista_alunos[0].notas.append(7.0)
    lista_alunos[0].faltas += 2

    lista_alunos[1].notas.append(5.5)
    lista_alunos[1].faltas += 6

    # O aluno no índice 2 ficará sem notas e sem faltas
    
    # Desafio extra: inativando o último aluno
    lista_alunos[-1].ativo = False

print("\n--- RELATÓRIO DE ALUNOS ---")

mais_faltas = None

# 3. Percorrendo a lista e calculando médias
for aluno in lista_alunos:
    print(f"\n{aluno.nome} ({aluno.matricula})")
    print(f"Notas: {aluno.notas}")
    print(f"Faltas: {aluno.faltas}")
    
    # Tratando aluno sem notas
    if len(aluno.notas) > 0:
        media = sum(aluno.notas) / len(aluno.notas)
        print(f"Média: {media:.2f}")
    else:
        print("Média: sem notas")
        
    # Lógica do "campeão de faltas"
    if mais_faltas is None or aluno.faltas > mais_faltas.faltas:
        mais_faltas = aluno

# 4. Exibindo o aluno com mais faltas
if mais_faltas is not None:
    print(f"\nMais faltas: {mais_faltas.nome} ({mais_faltas.faltas})")
else:
    print("\nNenhum aluno cadastrado.")

# Desafio extra: mostrando inativos separadamente
print("\n--- ALUNOS INATIVOS (Desafio Extra) ---")
for aluno in lista_alunos:
    if not aluno.ativo:
        print(f"{aluno.nome} está INATIVO.")