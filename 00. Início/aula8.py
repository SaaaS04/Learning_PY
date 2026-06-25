from datetime import date

nome = "Eu"
Sobrenome = "Aqui"
Idade = int(input("Digite sua idade: "))
ano_nascimeto = date.today().year - Idade
maior_idade = Idade > 18
altura = 1.89

print("Nome:", nome)
print("Sobrenome:", Sobrenome)
print("Idade:", Idade)
print("Ano do nascimento:", ano_nascimeto)
print("É maior de idade?", maior_idade)
print("Altura:", altura, end= "m")