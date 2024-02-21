def Adivinador(b, e, n):
  arreglo = []
  if b == e:
      return b
  for i in range(n):
      numero = b + ((e - b) // n) * (i + 1)
      arreglo.append(numero)
  for i in range(n):
      print("El numero", arreglo[i], "es Mayor(1), Menor(2) o Igual(otro) a tu numero?")
      respuesta = int(input())
      if respuesta == 1:
          if arreglo[i] < e:
              e = arreglo[i]
      elif respuesta == 2:
          if arreglo[i] > b:
              b = arreglo[i]
      else:
          return arreglo[i]
  return Adivinador(b, e, n)

while True:
  print("Hasta que numero quieres que se eliga?")
  e = int(input())
  print("Cuantos numeros quieres que adivine cada vez?")
  n = int(input())
  if e >= 0 and n >= 0:
      if(n>e):
       print("No puedo dividir en más partes que el numero de elementos")
      else:
       print("Piensa un numero del 0 al", e)
       print(Adivinador(0, e, n), "es tu numero!")
       break
  else:
      print("No puedes y no puedo pensar en numeros negativos")
