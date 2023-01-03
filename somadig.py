print()


print("Olá. Vou somar os dígitos de qualquer número inteiro que me fornecer.")


print()


entrada = int(input("Digite um número inteiro: "))


parcela = 0


soma = 0 


while (entrada) != 0:

	parcela = (entrada % 10)
	
	soma = soma + parcela

	entrada = (entrada // 10)

print()


print("A soma dos dígitos é", soma, ".")