# -*- coding:utf-8 -*-

import sys
import math

#Calcula distancia euclidiana entre duas cidades
def calcula_distancia(cidade1, cidade2):
    result = math.sqrt(pow(cidade2['x'] - cidade1['x'], 2) + pow(cidade2['y'] - cidade1['y'], 2))
    return round(result, 3)

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
        cidade = {'nome' : nome, 'x' : int(linha.split()[0]), 'y' : int(linha.split()[1])}
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
    print(lista_cidades[0])
    print(lista_cidades[0]['x'])
    print(calcula_distancia(lista_cidades[0], lista_cidades[1]))
    print("Concluido!")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))