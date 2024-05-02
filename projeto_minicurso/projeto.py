import pandas as pd

#importar base de dados 

tabela_vendas = pd.read_excel("C:/Users/aspdiogo/Documents/workspace/projeto_minicurso/vendas.xlsx")

#visualizar base de dados 

pd.set_option('display.max_columns', None)
print(tabela_vendas)

#faturamento por loja 

#quantidade de produtos por loja

#ticket médio por produto em cada loja

#enviar email com relatório