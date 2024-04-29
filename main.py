def soma(valor1, valor2):
    return valor1 + valor2

def multiplicacao(valor1, valor2):
    return valor1 * valor2
def divisao(valor1, valor2):
    return valor1 / valor2
while True:

    resultado = input("para soma digite 1, multiplição 2, divisão 3:  ")
    
    valor1 = float(input("primeiro valor: "))
    
    valor2 = float(input("segundo valor: "))
    
    if resultado == "1":

        resposta = soma(valor1, valor2)
        print(valor1, "+", valor2, "=", resposta)
    
    elif resultado == "3":
        resposta3 = divisao(valor1, valor2)
        print(valor1, "/", valor2, "=", resposta3)

    else:

        resposta2 = multiplicacao(valor1, valor2)
        print(valor1, "x", valor2, "=", resposta2)
        
    
    
    