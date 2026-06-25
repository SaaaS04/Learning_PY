# nome = "Otávio"

# print(nome[2])
# print(nome[-3])

# print('v' in nome)
# print('z' in nome)
# print(10 * "-")
# print('vio' not in nome)
# print('zero' in nome)

nome = input("Digite o seu nome: \n")
encontrar = input("Digite o que deseja encontrar: \n")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else: 
    print(f"{encontrar} não está em {nome}")