import pandas as pd

#importar base de dados 

tabela_vendas = pd.read_excel("C:/Users/aspdiogo/Documents/workspace/projeto_minicurso/vendas.xlsx")

#visualizar base de dados 

pd.set_option('display.max_columns', None)


#faturamento por loja 

faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()

print(faturamento)

#quantidade de produtos por loja

Quant_D_Produtos = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()

print(Quant_D_Produtos)

#ticket médio por produto em cada loja

#enviar email com relatório