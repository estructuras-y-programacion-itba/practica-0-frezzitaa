def generala(d1,d2,d3,d4,d5):
    generala=False
    
    if d1==d2==d3==d4==d5:
        generala=True    
        return generala
    else:
        return generala #validar despeus enn otrae funcion si el turno es igiual a 1 o no


def escalera(d1,d2,d3,d4,d5):
    escalera=False
    lista=[d1,d2,d3,d4,d5]
    lista.sort() #ordena de menor a mayor
    
    for i in range(len(lista)-1):
        if lista[i]+1!=lista[i+1]:
            return escalera
        
    escalera=True
    return escalera
        

def poker(d1,d2,d3,d4,d5):
    poker=False
    lista=[d1,d2,d3,d4,d5]
    
    for numero in lista:
        contador=0
        for i in range(len(lista)):
            if numero==lista[i]:
                contador+=1
                if contador==4:
                    poker=True
                    
    return poker
            
            
def full(dados):
    valores_unicos = set(dados)
    if len(valores_unicos) != 2:
        return False
    cantidad = dados.count(dados[0])
    return cantidad in [2, 3]


def numero_ind(d1, d2, d3, d4, d5):
    lista = [d1, d2, d3, d4, d5]
  
    n1=lista.count(1)*1
    n2=lista.count(2)*2
    n3=lista.count(3)*3
    n4=lista.count(4)*4
    n5=lista.count(5)*5
    n6=lista.count(6)*6
    
    return [n1, n2, n3, n4, n5, n6]
            
    

def tiradas ():
    import random
    turno=1
    decision=''
    d1=0
    d2=0
    d3=0
    d4=0
    d5=0
    des1='si'
    des2='si'
    des3='si'
    des4='si'
    des5='si'
    while turno<3 and decision!='fin' :
        if des1=='si':
            d1=random.randint(1,5)
            print (d1)
        if des2=='si':
            d2=random.randint(1,5)
            print (d2)
        if des3=='si':
            d3=random.randint(1,5)
            print(d3)
        if des4=='si':
            d4=random.randint(1,5)
            print (d4)
        if des5=='si':
            d5=random.randint(1,5)
            print (d5)
        if des1!='no':
            des1= input('escriba "si" para volver a tirar y "no" fijar el dado 1.')
        if des2!='no':
            des2= input('escriba "si" para volver a tirar y "no" fijar el dado 2.') 
        if des3!='no':
            des3= input('escriba "si" para volver a tirar y "no" fijar el dado 3.')   
        if des4!='no':
            des4= input('escriba "si" para volver a tirar y "no" fijar el dado 4.')
        if des5!='no':
            des5= input('escriba "si" para volver a tirar y "no" fijar el dado 5.') 
        turno+=1               
        desicion= input('escriba "fin" para finalizar el turno o deje vacio.')
    dados=[d1,d2,d3,d4,d5]
    return turno,dados
            
            
            sEse'( tupni =
    desicion     

Ese'( tupni =
    desicion     

Ese'( tupni =
    desicion     

Ese'( tupni =
    desicion     

Ese'( tupni =
    desicion     

    
                 
      





def juego_terminado(listaj1, listaj2):
    
    if len(listaj1) == 10 and len(listaj2) == 10:
        return True
    return False
#if endgame(jugadas_j1, jugadas_j2):
#print("\n¡Ambos jugadores completaron la planilla!")


def registrar_combinacion(combinacion_elegida, combinaciones_usadas):
    if combinacion_elegida not in   combinaciones_usadas:
        combinaciones_usadas.append(combinacion_elegida)    
    return combinaciones_usadas
    
    

def main():
    