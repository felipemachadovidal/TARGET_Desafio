def is_fibonacci(num):
    if num == 0 or num == 1:
        return True

    a, b = 0, 1
    while b < num:
        a, b = b, a + b

    return b == num

numero = 21
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
