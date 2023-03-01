#estrutura condicional
hora: int

hora = int(input('Digite uma hora do dia: '))

if hora < 12:
    print('Bom dia!')
elif hora < 18:
    print('Boa tarde!')
else:
    print('Boa noite!')

#estrutura repetitiva enquanto
x: int
soma: int

soma = 0
x = int(input('Digite o primeiro número: '))

while x != 0:
    soma = soma + x
    x = int(input('Digite outro número: '))

print('SOMA = ', soma)

#estrutura repetitiva para
N = int(input('Quantos números serão digitados? '))
soma = 0

for i in range(0, N):
    x = int(input('Digite um número: '))
    soma = soma + x

print('SOMA = ', soma)

#vetores
N = int(input('Quantos números você vai digitar? '))
vet: [float] = [0 for x in range (N)]

for i in range(0,N):
    vet[i] = float(input('Digite um número: '))

print()
print('NÚMEROS DIGITADOS:')
for i in range(0,N):
    print(f'{vet[i]:.1f}')

#matrizes
M = int(input('Quantas linhas vai ter a matriz? '))
N = int(input('Quantas colunas vai ter a matriz? '))

mat: [[int]] = [[0 for x in range(N)] for x in range(M)]

for i in range(0,M):
    for j in range(0,N):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print('MATRIZ DIGITADA:')
for i in range(0,M):
    for j in range(0,N):
        print(f'{mat[i][j]} ', end='')
    print()
