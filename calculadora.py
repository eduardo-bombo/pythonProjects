print('Calculadora:')
print('(+) Adição')
print('(-) Subtração')
print('(*) Multiplicação')
print('(/) Divisão')
op = input('Qual operação deseja fazer? ')
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
if (op == '+'):
  res = x + y
  print('Resultado: {} + {} = {}'.format(x, y, res))
elif (op == '-'):
  res = x - y
  print('Resultado: {} - {} = {}'.format(x, y, res))
elif (op == '*'):
  res = x * y
  print('Resultado: {} * {} = {}'.format(x, y, res))
elif (op == '/'):
  res = x / y
  print('Resultado: {} / {} = {}'.format(x, y, res))
else:
  print('Operação inválida.')