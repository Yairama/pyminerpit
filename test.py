
letra = input("letra: ")
print("No se puede procesar el dato" if (len(letra)) != 1 else ("vocal" if letra in ('a','e','i','o','u') else "consonante"))
