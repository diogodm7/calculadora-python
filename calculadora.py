#funções

def funcsoma(valor1, valor2):
    return valor1 + valor2 

def multiplicacao(valor1, valor2):
    return valor1 * valor2

def divisao(valor1, valor2):
    return valor1 / valor2
#parte de ação 

while True:

    resultado = input("para somar digite 1, multiplicar 2, dividir 3: ")


    valor1 = float(input("digite o primeiro valor: "))
    
    valor2 = float(input("digite o segundo valor: "))
     
    if resultado == "2":
        
        resposta2 = multiplicacao(valor1, valor2)
        print(valor1, "x", valor2, "=", resposta2)
    
    elif resultado == "3":
        resposta3 = divisao(valor1, valor2)
        print(valor1, "/", valor2, "=", resposta3)

    else:
        resposta = funcsoma(valor1, valor2)
        print(valor1, "+", valor2, "=", resposta)

    print("uso da git")