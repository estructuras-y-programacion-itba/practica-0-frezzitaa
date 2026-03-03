def generala(lista):
    generala=False
    
    if lista[0]==lista[1]==lista[2]==lista[3]==lista[4]:
        generala=True    
        return generala
    else:
        return generala #validar despeus enn otrae funcion si el turno es igiual a 1 o no


def escalera(lista):
    escalera=False
    lista.sort() #ordena de menor a mayor
    
    for i in range(len(lista)-1):
        if lista[i]+1!=lista[i+1]:
            return escalera
        
    escalera=True
    return escalera
        

def poker(lista):
    poker=False
    for numero in lista:
        contador=0
        for i in range(len(lista)):
            if numero==lista[i]:
                contador+=1
                if contador==4:
                    poker=True
                    
    return poker
            
            
def full(lista):
    valores_unicos = set(lista)
    if len(valores_unicos) != 2:
        return False
    cantidad = lista.count(lista[0])
    return cantidad in [2, 3]


def numero_ind(lista):
    
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
        while turno<=3:
            if des1!='no' and turno!=1:
                des1= input('escriba "si" para volver a tirar y "no" fijar el dado 1.')
            if des2!='no' and turno!=1:
                des2= input('escriba "si" para volver a tirar y "no" fijar el dado 2.') 
            if des3!='no' and turno!=1:
                des3= input('escriba "si" para volver a tirar y "no" fijar el dado 3.')   
            if des4!='no' and turno!=1:
                des4= input('escriba "si" para volver a tirar y "no" fijar el dado 4.')
            if des5!='no' and turno!=1:
                des5= input('escriba "si" para volver a tirar y "no" fijar el dado 5.') 
            if turno!=1:
                decision= input('escriba "fin" para finalizar el turno o deje vacio.')
            if decision=='fin':
                break
            turno+=1
            if des1=='si':
                d1=random.randint(1,6)
                print ('valor 1= ' + str(d1))
            if des2=='si':
                d2=random.randint(1,6)
                print ('valor 2= ' + str(d2))
            if des3=='si':
                d3=random.randint(1,6)
                print('valor 3= ' + str(d3))
            if des4=='si':
                d4=random.randint(1,6)
                print ('valor 4= ' + str(d4))
            if des5=='si':
                d5=random.randint(1,6)
                print ('valor 5= ' + str(d5))
        dados=[d1,d2,d3,d4,d5]
        turno-=1
        return turno,dados    



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
    


def guardar_csv(planilla_j1, planilla_j2):
    categorias = ['E', 'F', 'P', 'G', '1', '2', '3', '4', '5', '6']
    with open('jugadas.csv', 'w') as f:
        f.write("jugada,j1,j2\n")
        for cat in categorias:
            p1 = planilla_j1.get(cat, 0)
            p2 = planilla_j2.get(cat, 0)
            f.write(f"{cat},{p1},{p2}\n")

def main(): #boceto con gemini
    planilla_j1 = {}
    planilla_j2 = {}
    
    categorias_numeros = ['1', '2', '3', '4', '5', '6']
    categorias_mayores = ['E', 'F', 'P', 'G']
    
    print("--- BIENVENIDOS A LA GENERALA ---")

    while not juego_terminado(planilla_j1, planilla_j2):
        for j in range(1, 3):
            planilla_actual = planilla_j1 if j == 1 else planilla_j2
            
            if len(planilla_actual) == 10:
                continue

            print(f"\nTURNO DEL JUGADOR {j}")
            tirada_final, dados = tiradas()
            es_servido = (tirada_final == 0)
            
            print(f"Dados finales del Jugador {j}: {dados}")

            if generala(dados) and es_servido:
                print(f"¡GENERALA REAL! El Jugador {j} gana automáticamente.")
                planilla_actual['G'] = 80 
                guardar_csv(planilla_j1, planilla_j2)
                return

            disponibles = [c for c in (categorias_numeros + categorias_mayores) if c not in planilla_actual]
            print(f"Categorías pendientes: {disponibles}")
            
            eleccion = input("Elija categoría para anotar: ").upper()
            while eleccion not in disponibles:
                eleccion = input("Invalida o ya usada. Elija de nuevo: ").upper()

            puntos = 0
            if eleccion == 'G':
                if generala(dados): puntos = 50
            elif eleccion == 'P':
                if poker(dados): puntos = 40 + (5 if es_servido else 0)
            elif eleccion == 'F':
                if full(dados): puntos = 30 + (5 if es_servido else 0)
            elif eleccion == 'E':
                if escalera(dados): puntos = 20 + (5 if es_servido else 0)
            elif eleccion in categorias_numeros:
                totales_num = numero_ind(dados)
                puntos = totales_num[int(eleccion) - 1]

            planilla_actual[eleccion] = puntos
            guardar_csv(planilla_j1, planilla_j2)
            print(f"Anotado: {puntos} puntos en {eleccion}.")

    total_j1 = sum(planilla_j1.values())
    total_j2 = sum(planilla_j2.values())
    print("\n--- FIN DEL JUEGO ---")
    print(f"Puntaje Final J1: {total_j1}")
    print(f"Puntaje Final J2: {total_j2}")
    
    if total_j1 > total_j2: print("¡Gana el Jugador 1!")
    elif total_j2 > total_j1: print("¡Gana el Jugador 2!")
    else: print("¡Empate!")

if __name__ == "__main__":
    main()    