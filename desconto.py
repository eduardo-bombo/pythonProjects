preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o percentual de desconto: '))

desconto = preco * (p/100)
final = preco - desconto

print('O preço do produto é {}. Desconto de {}%.'.format(preco, p))
print('Valor calculado de desconto: {}. O valor final é de: R${}.'.format(desconto, final))