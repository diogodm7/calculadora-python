#funções

def funcsoma(valor1, valor2):
    return valor1 + valor2 

def multiplicacao(valor1, valor2):
    return valor1 * valor2

def divisao(valor1, valor2):
    return valor1 / valor2

def subtracao(valor3, valor4):
    return valor3, valor4

#parte de ação 

while True:

    resultado = input("para somar digite 1, multiplicar 2, dividir 3: ")


    
    
    valor3 =  float(input("diga o minuendo: "))

    valor4 = float(input("diga o subtraendo: "))



    
    
    if resultado == "2":

        valor5 = float(input("diga o multiplicado: "))

        valor6 = float(input("diga o multiplicador"))

        valor1 = float(input("diga a primeira parcela: "))
        resposta2 = multiplicacao(valor1, valor2)
        print(valor1, "x", valor2, "=", resposta2)
    
    elif resultado == "3":
             
        valor7 = float(input("diga o dividendo: "))

        valor8 = float(input("diga o divisor: "))

        resposta3 = divisao(valor1, valor2)
        print(valor1, "/", valor2, "=", resposta3)

    else: 

        valor1 = float(input("diga a primeira parcela: "))
    
        valor2 = float(input("diga a segunda parcela: "))

        resposta = funcsoma(valor1, valor2)
        print(valor1, "+", valor2, "=", resposta)

    