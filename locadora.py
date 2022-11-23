km = int(input("Qual foi a quantidade de Km percorridos? "))
dias = int(input("Por quantos dias o carro foi alugado? "))

valor = (60 * dias) + (0.15 * km)

print('O valor a ser pego pelo aluguel do automóvel é de {}.'.format(valor))