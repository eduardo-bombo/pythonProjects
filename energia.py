print('Conta de Energia')
print('R para residencial')
print('C para comercial')
print('I para industrial')
tipo_imovel = input('Qual o tipo de unidade consumidora? ')
kWh = float(input('Quantos kWh foram consumidos? '))
if tipo_imovel == 'R':
    if kWh <= 500:
        valor = kWh * 0.4
    else:
        valor = kWh * 0.65
elif tipo_imovel == 'C':
    if kWh <= 1000:
        valor = kWh * 0.55
    else:
        valor = kWh * 0.60
elif tipo_imovel == 'I':
    if kWh <= 5000:
        valor = kWh * 0.55
    else:
        valor = kWh * 0.60
else:
    print('Instalação inválida. Encerrando o programa.')
print('Valor da sua conta de energia: R${}.'.format(valor))