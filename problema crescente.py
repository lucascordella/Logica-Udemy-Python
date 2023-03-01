print('Digite dois números:')
X = int(input())
Y = int(input())

while X != Y:
    if X < Y:
        print('CRESCENTE!')
    elif X > Y:
        print('DECRESCENTE!')

    print('Digite outros dois números:')
    X = int(input())
    Y = int(input())