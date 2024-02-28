def fibonacci_iterativo(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a + b
  return a

numero = 30
resultado = fibonacci_iterativo(numero)
print(f"El {numero}-ésimo número de Fibonacci es: {resultado}")

