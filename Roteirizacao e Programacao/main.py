matriz_distancias = [
    [10000, 5, 2, 7, 6, 7, 8],
    [5, 10000, 5, 3, 12, 13, 8],
    [2,5, 10000, 3,6,7,4],
    [7,3,3,10000,8,9,4],
    [6,12,6,8,10000,2,7],
    [7,13,7,9,2,10000,4],
    [8,8,4,4,7,4,10000]
]

# VIZINHO MAIS PRÓXIMO PARA OBTER A SOLUÇÃO INICIAL

vetor_rota = [0]*(len(matriz_distancias[0])+1)
print("Quantidade de nós do problema:",len(matriz_distancias[0]))
no_origem = int(input ("Digite o nó de origem: "))
vetor_rota[0] = no_origem
vetor_rota[len(matriz_distancias[0])] = no_origem


custo_total = 0
nos_disponiveis = [0]*len(matriz_distancias[0])
for i in range (0, len(matriz_distancias[0])):
    nos_disponiveis[i] = i+1


nos_disponiveis.remove(no_origem)


vizinho_mais_proximo = 0
custo_vizinho = 100

contador = 0
contador_vetor_rota = 1 #inicia em 1, pois o nó de origem já foi colocado

while(contador<len(matriz_distancias[0])-1):
    while nos_disponiveis:
        for no in nos_disponiveis:
            if matriz_distancias[no_origem-1][no-1] < custo_vizinho:
                vizinho_mais_proximo = no
                custo_vizinho = matriz_distancias[no_origem-1][no-1]
        
        no_origem = vizinho_mais_proximo 
        nos_disponiveis.remove(no_origem)
        custo_total += custo_vizinho
        vetor_rota[contador_vetor_rota]= vizinho_mais_proximo
        contador += 1 
        contador_vetor_rota += 1
        vizinho_mais_proximo = 0 
        custo_vizinho = 100

    
custo_total += matriz_distancias[no_origem-1][vetor_rota[0]-1]

print(vetor_rota)
print ("custo total:", custo_total)

# VND

