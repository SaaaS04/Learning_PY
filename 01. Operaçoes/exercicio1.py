primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Outro valor: ")

if primeiro_valor > segundo_valor:
    print(f"O primeiro valor: {primeiro_valor}")
    print(f"é maior queo segundo valor: {segundo_valor}")
elif segundo_valor > primeiro_valor:
     print(f"O segundo valor: {segundo_valor}")
     print(f" é maior queo primeiro valor: {primeiro_valor}")
else: print("Os valores sao iguais")