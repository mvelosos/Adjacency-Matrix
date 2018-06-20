from beautifultable import BeautifulTable
import numpy as np

vertices = []

#Recebendo os Inputs
while(True):
    vo = input('Vertice de Origem: ')
    while(vo == ''):
        print('Campo dever ser preenchido!')
        vo = input('Vertice de Origem: ')
        
    if(vo == '.'):
        break
    
    vd = input('Vertice de Destino: ')
    while(vd == ''):
        print('Campo dever ser preenchido!')
        vd = input('Vertice de Destino: ')
        
    pa = input('Peso da Aresta: ')
    while(pa == ''):
        print('Campo dever ser preenchido!')
        pa = input('Peso da Aresta: ')

    con = [vo.upper(), vd.upper(), pa]
    vertices.append(con)

    print(len(vertices))
    print(vertices)
    for x in range(len(vertices[:-1])):
        if(con[0] == vertices[x][0]):
            if(con[1] == vertices[x][1]):
               print('Invalido! Já existe uma aresta conectando ', con[0],'->',con[1])
               vertices.pop()

#Coletando cada vértice             
letras = []
for l in range(len(vertices)):
    for m in range(len(vertices[-1])):
        if(vertices[l][m] not in letras):
            letras.append(vertices[l][m])

#Removendo números da lista dos vértices
alfa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for x in letras:
    if(x not in alfa):
        letras.remove(x)

#Ordenando a lista de vértices
letras.sort()
print(letras)

#Criando a Matriz
table = BeautifulTable()

mtx = np.matrix([])

table.column_headers = letras
for i in range(len(letras)):
    mtx = np.append(mtx, letras)
    mtx.fill(-1)
    table.append_row(mtx[:(len(letras))])
table.insert_column(0, ' ', letras)

print(table)
#print(mtx, axis=len(letras))

aa = np.matrix([[1,2],[3,4]])
ab = np.array([[1,2],[3,4]])

print(aa)
print(ab)
print(mtx)















