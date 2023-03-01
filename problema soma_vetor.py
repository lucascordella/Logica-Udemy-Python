N = int(input('Quantos números você vai digitar? '))
vet: [float] = [0 for x in range(N)]

soma = 0
for i in range(0,N):
    vet[i] = float(input('Digite um número: '))
    soma = soma + vet[i]

print()
print('VALORES = ', end= ' ')
for i in range(0,N):
    print(f'{vet[i]}', end= ' ')

print()
print(f'SOMA = {soma:.2f}')

media = soma / N
print(f'MEDIA = {media:.2f}')