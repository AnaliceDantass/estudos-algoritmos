def buscaMenor(arr):
  menor = [0]
  menor_indice = 0
  for i in range(1, len(arr)):
    if arr[1] < menor:
      menor = arr[i]
      menor_indice = i
  return menor_indice

def ordenacaoporSelecao(arr):
  novoArr = []
  for i in range(len(arr)):
    menor = buscaMenor(arr)
    novoArr.append(arr.pop(menor))
  return novoArr
print ordenacaoporSelecao([5, 3, 6, 2, 10])

