# -*- coding:utf-8 -*-

import sys
import math

#Calcula distancia euclidiana entre duas cidades
def calcula_distancia(cidade1, cidade2):
    result = math.sqrt(pow(cidade2['x'] - cidade1['x'], 2) + pow(cidade2['y'] - cidade1['y'], 2))
    return round(result, 3)

def vizinho_mais_proximo(grafo):

    grafo[0]['visitado'] = True
    vertice_atual = grafo[0]
    tamanho_grafo = len(grafo)
    menor_distancia = calcula_distancia(vertice_atual, grafo[1])
    resposta = []
    resposta.append(grafo[0])
    total = 0

    while len(resposta) < tamanho_grafo:
        i = 0
        while i < tamanho_grafo:
            if not grafo[i]['visitado']:
                distancia = calcula_distancia(vertice_atual, grafo[i])
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    vertice_atual = grafo[i]
                    i += 1
            i += 1
        resposta.append(vertice_atual)
        vertice_atual['visitado'] = True
        total += menor_distancia
        menor_distancia = 9999999999
        
    
    print(total)

    return resposta

def main(args):
    #checa se os argumentos .
    if(len(args) != 3):
        print("Número de argumentos errado")
        print("Use: <programa.py> <entrada.dat> <numero de caixeiros>")
        sys.exit()
    
    #Argumentos do programa.
    nome_entrada = args[1]
    numero_caixeiros = int(args[2])

    #Pega numero de cidades.
    arqv_entrada = open(nome_entrada, 'r')
    numero_cidades = int(arqv_entrada.readline())
    lista_cidades = []

    #Pega as coordenadas de cada cidade, uma cidade é um dicionario com nome, coordenada x e
    #coordenada y.
    nome = 0
    for linha in arqv_entrada.readlines()[slice(numero_cidades)]:
        cidade = {'nome' : nome, 'visitado' : False, 'x' : int(linha.split()[0]), 'y' : int(linha.split()[1])}
        lista_cidades.append(cidade)
        nome += 1
    
    #Fecha o arquivo de entrada.
    arqv_entrada.close()

    #Cria arquivo de saida
    #arqv_saida = open(nome_saida, 'w')
    #arqv_saida.write(str(list_size) + "\n")

    #for number in number_list:
    #    arqv_saida.write(str(number) + "\n")
    
    #testes
    result = vizinho_mais_proximo(lista_cidades)
    for cidade in result:
        print(cidade['nome'])
    print("Concluido!")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))