from heapq import heapify, heappush 
from random import randint, uniform
import operator
import time
import timeit  

inicio = timeit.default_timer()
elementos = 1000
N = []

# 1. crie uma estrutura de registro composta de dois valores: distância e classe.
class EstruturaRegistro:
    def __init__(self, distancia, classe):
        self.classe = classe
        self.distancia = distancia
    
    def __lt__(self, other):
        return self.distancia < other.distancia

# 2. gere randomicamente N=1000 registros, com a distância float podendo variar 
# entre 0.0 e 100.0, e a classe podendo ter apenas três valores inteiros: 1, 2, ou 3.
for x in range(elementos):
    y = EstruturaRegistro(round(uniform(0.0, 100.0),2), randint(1,3))
    N.append(y)

# https://docs.python.org/3/library/operator.html
# Provided itemgetter(0) is O(1) when used with data, the sort is O(n log n) both on average and in the worst case.
# https://en.wikipedia.org/wiki/Timsort
N.sort(key=operator.attrgetter('distancia'))

# Criar uma heap vazia 
heap = [] 
heapify(heap) 
  
# 3. insira todos os 1000 registros em uma min-Heap de tamanho 15, 
# com a chave sendo a distância, descartando os que caírem fora da Heap
for x in range(15):
    # heappush(heap, operator.attrgetter('distancia')(N[x])) 
    heappush(heap, N[x])

# imprimindo o valor do elemento mínimo
print("Valor principal da pilha : " + str(heap[0].distancia) + "\n")
  
# 4. imprima os 15 elementos da Heap no final. Distância e classe.
print("Os elementos da pilha: ") 
for i in heap: 
    print("distancia: ", i.distancia , " classe: ", i.classe) 

# for x in range(elementos):
#     print("Distancia: " + str(N[x].distancia) +" - Classe:"+str(N[x].classe) )

fim = timeit.default_timer()
print ('duração da execução: %f segundos' % (fim - inicio))