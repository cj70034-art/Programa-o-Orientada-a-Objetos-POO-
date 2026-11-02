from televisao import Televisao

# 1. Criando os objetos e guardando na lista
tv1 = Televisao("Samsung", 43)
tv2 = Televisao("LG", 50)
tv3 = Televisao("Philco", 32)

lista_tvs = [tv1, tv2, tv3]

# 2. Alterando atributos diretamente
tv1.ligada = True
tv2.ligada = True
# tv3 continua desligada

tv1.canal = 5
tv1.volume = 25

tv2.canal = 12
tv2.volume = 70

#Desafio extra: adicionando favoritos apenas na tv2
tv2.favoritos.append(12)
tv2.favoritos.append(5)

# 3. Variáveis para os cálculos (campeão da quadra, contadores)
qtd_ligados = 0
maior_tv = None
soma_polegadas = 0

print("--- LISTAGEM DE TELEVISORES ---")

# 4. Percorrendo a lista
for tv in lista_tvs:
    if tv.ligada:
        print(f'{tv.marca} {tv.polegadas}" | Ligada | Canal {tv.canal} | Volume {tv.volume}')
        qtd_ligados += 1
    else:
        print(f'{tv.marca} {tv.polegadas}" | Desligada')
    
    # Lógica para a soma e para achar o maior
    soma_polegadas += tv.polegadas
    if maior_tv is None or tv.polegadas > maior_tv.polegadas:
        maior_tv = tv

# 5. Estatísticas finais
media_polegadas = soma_polegadas / len(lista_tvs)

print("\n--- ESTATÍSTICAS ---")
print(f"Televisores ligados: {qtd_ligados}")
print(f'Maior televisor: {maior_tv.marca} {maior_tv.polegadas}"')
print(f"Média de polegadas: {media_polegadas:.2f}")

# Teste visual do desafio extra
print("\n--- FAVORITOS (Desafio Extra) ---")
print(f"Favoritos da {tv2.marca}: {tv2.favoritos}")
print(f"Favoritos da {tv1.marca}: {tv1.favoritos} (prova de que são independentes)")