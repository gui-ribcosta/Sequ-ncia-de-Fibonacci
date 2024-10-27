def pertence_fibonacci(n):
    a, b = 0, 1
    fib = [a, b]  # Lista para armazenar a sequência
    while b < n:
        a, b = b, a + b
        fib.append(b)
    return n in fib

# Entrada do usuário
numero = int(input("Informe um número: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
