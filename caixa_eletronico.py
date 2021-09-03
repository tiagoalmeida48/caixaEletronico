saque = int(input('Digite o valor do saque: '))
notas_1 = notas_5 = notas_10 = notas_50 = notas_100 = 0
notas1_str = notas5_str = notas10_str = notas50_str = notas100_str = ''

if saque >= 10 & saque <= 600:
    if saque >= 100:
        notas_100, saque = divmod(saque, 100)
        notas100_str = '1 nota de 100 reais ' if notas_100 == 1 else f'{notas_100} notas de 100 reais '
    if saque >= 50 & saque < 100:
        notas_50, saque = divmod(saque, 50)
        notas50_str = '1 nota de 50 reais ' if notas_50 == 1 else f'{notas_50} notas de 50 reais '
    if saque >= 10 & saque < 50:
        notas_10, saque = divmod(saque, 10)
        notas10_str = '1 nota de 10 reais ' if notas_10 == 1 else f'{notas_10} notas de 10 reais '
    if saque >= 5 & saque < 10:
        notas_5, saque = divmod(saque, 5)
        notas5_str = '1 nota de 5 reais ' if notas_5 == 1 else f'{notas_5} notas de 5 reais '
    if saque >= 1 & saque < 5:
        notas_1, saque = divmod(saque, 1)
        notas1_str = '1 nota de 1 reais ' if notas_1 == 1 else f'{notas_1} notas de 1 reais '
else:
    print('O valor de saque minimo é de 10 reais e o valor máximo é de 600 reais')

print(notas100_str)
print(notas50_str)
print(notas10_str)
print(notas5_str)
print(notas1_str)