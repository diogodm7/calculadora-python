#funções
def funcsoma(valor1, valor2):
    return valor1 + valor2 

def multiplicacao(valor5, valor6):
    return valor5 * valor6

def divisao(valor7, valor8):
    return valor7 / valor8

def subtracao(valor3, valor4):
    return valor3 - valor4

def potencia(valor9, valor10):
    return valor9 ** valor10

#parte de ação 

while True:

    resultado = input("para somar digite 1, multiplicar 2, dividir 3, subtrair 4: ")

    
    if resultado == "2":

        valor5 = float(input("diga o multiplicado: "))

        valor6 = float(input("diga o multiplicador: "))

        resposta2 = multiplicacao(valor5, valor6)

        print(valor5, "x", valor6, "=", resposta2)
    
    elif resultado == "3":
             
        valor7 = float(input("diga o dividendo: "))

        valor8 = float(input("diga o divisor: "))

        resposta3 = divisao(valor7, valor8)

        print(valor7, "/", valor8, "=", resposta3)

    elif resultado == "4":
        
        valor3 = float(input("diga o minuedo: "))
        
        valor4 = float(input("diga o subtraendo: "))

        resposta4 = subtracao(valor3, valor4)

        print(valor3, "-", valor4, "=", resposta4)
        
    

    else: 

        valor1 = float(input("diga a primeira parcela: "))
    
        valor2 = float(input("diga a segunda parcela: "))

        resposta = funcsoma(valor1, valor2)
        
        print(valor1, "+", valor2, "=", resposta)