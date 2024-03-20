def verifica(numero):
    fib1 = 0
    fib2 = 1
    if numero == fib1 or numero == fib2:
        return True
    while fib2 <= numero:
        fib1, fib2 = fib2, fib1 + fib2
        if fib2 == numero:
            return True
    return False

def teste(numero):
    if verifica(numero):
        print(f'O número {numero} pertence à sequência de Fibonacci.')
        print()
    else:
        print(f'O número {numero} não pertence à sequência de Fibonacci.')
        print()

print()
numeroInf = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
print()
teste(numeroInf)
