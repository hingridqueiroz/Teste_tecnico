def fibonacci(n):
    fib_sequencia = [0, 1]
    while fib_sequencia[-1] < n:
        fib_sequencia.append(fib_sequencia[-1] + fib_sequencia[-2])
    return fib_sequencia

def checar_sequencia(number):
    sequencia = fibonacci(number)
    if number in sequencia:
        print(f"{number} pertence à sequência")
    else:
        print(f"{number} NÃO pertence à sequência")

numero = int(input("Digite um número: "))
mensagem = checar_sequencia(numero)
