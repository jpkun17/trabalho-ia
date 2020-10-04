# -*- coding:utf-8 -*-

import sys
import math
import numpy

#################################################################################################
# Calcula distância euclidiana entre duas cidades.
#################################################################################################

def calcula_distancia(cidade1, cidade2):
    result = math.sqrt(pow(cidade2['x'] - cidade1['x'], 2) + pow(cidade2['y'] - cidade1['y'], 2))
    return round(result, 3)

#################################################################################################
# Parte uma lista em N partes.
#################################################################################################

def parte_lista(seq, size):
    return (seq[i::size] for i in range(size))

#################################################################################################
# Algoritmo do Vizinho Mais Próximo (greedy algorithm)
#################################################################################################

def vizinho_mais_proximo(grafo):

    #Iniciação das variáveis
    tamanho_grafo = len(grafo)
    vertice_atual = grafo[0]
    vertice_atual['visitado'] = True
    lista_visitas = []
    lista_visitas.append(grafo[0])
    menor_distancia = calcula_distancia(vertice_atual, grafo[1]) #distância inicial arbitrária
    destino = grafo[1] #destino inicial arbitrário
    distancia_percorrida = 0

    #execução do algoritmo
    while len(lista_visitas) < tamanho_grafo:
        i = 0
        while i < tamanho_grafo:
            if not grafo[i]['visitado']:
                distancia = calcula_distancia(vertice_atual, grafo[i])
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    destino = grafo[i]
                    i += 1
            i += 1
        vertice_atual = destino
        vertice_atual['visitado'] = True
        lista_visitas.append(vertice_atual)
        distancia_percorrida += menor_distancia
        menor_distancia = float('inf') #qualquer valor é menor que infinito
    
    #Adiciona o valor a distancia para voltar para a primeira cidade
    distancia_percorrida += calcula_distancia(vertice_atual, grafo[0])

    #printa a ordem que as cidades foram visitadas (apenas pra testes)
    for item in lista_visitas:
        print(item['nome'])
    print("--------")

    return round(distancia_percorrida, 3)

#################################################################################################
# Método responsável por dividir o grafo para N caixeiros e coletar suas distâncias percorridas.
#################################################################################################

def n_caixeiros(grafo, caixeiros):

    primeira_cidade = grafo[0]
    distancia_maxima_dia = 600
    custo_diaria = 150
    distancia_cada_caixeiro = []
    distancia_total = 0
    dias_cada_caixeiro = []
    custo_cada_caixeiro = []
    custo_total = 0

    lista_subgrafos = list(parte_lista(grafo, caixeiros))

    #Adiciona a primeira cidade aos subgrafos que não a têm (indice 1 em diante)
    #já que todos saem da cidade 0
    i = 1
    while i < len(lista_subgrafos):
        lista_subgrafos[i].insert(0, primeira_cidade)
        i += 1

    #Calcula os dados de cada caixeiro
    for subgrafo in lista_subgrafos:
        retorno = vizinho_mais_proximo(subgrafo)
        distancia_cada_caixeiro.append(retorno)
        dias = int(retorno/distancia_maxima_dia)
        dias_cada_caixeiro.append(dias)
        custo = dias * custo_diaria
        custo_cada_caixeiro.append(custo)
        distancia_total += retorno
        custo_total += custo

    #Testes
    print(distancia_cada_caixeiro)
    print(distancia_total)
    print(dias_cada_caixeiro)
    print(custo_cada_caixeiro)
    print(custo_total)

#################################################################################################
# Main
#################################################################################################

def main(args):
    #checa se os argumentos estão corretos.
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
    
    #testes
    n_caixeiros(lista_cidades,numero_caixeiros)
    print("Concluido!")

    return 0

#Executa a função main
sys.exit(main(sys.argv))