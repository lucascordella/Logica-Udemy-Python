print('Digite dois números:')
X = int(input())
Y = int(input())

soma = 0
if X > Y:
    troca = X
    X = Y
    Y = troca

for i in range(X+1,Y):
    if i % 2 != 0:
        soma = soma + i

print(f'SOMA DOS IMPARES = {soma}')