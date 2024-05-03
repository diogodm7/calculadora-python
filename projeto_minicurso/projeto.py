import pandas as pd
import win32com.client as win32
#importar base de dados 

tabela_vendas = pd.read_excel("C:/Users/aspdiogo/Documents/workspace/projeto_minicurso/vendas.xlsx")

#visualizar base de dados 

pd.set_option('display.max_columns', None)


#faturamento por loja 

faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()

print(faturamento)

#quantidade de produtos por loja

Quantidade = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()

print(Quantidade)

print('-' * 50)

#ticket médio por produto em cada loja

ticket_medio = (faturamento['Valor Final'] / Quantidade['Quantidade']).to_frame()

print(ticket_medio)

#enviar email com relatório

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'diogominion7@gmail.com'
mail.Subject = 'Relatório de Vendas de uma loja de testes'
mail.HTMLBody = f'''
<p>Prezados.</p>

<p>Segue o relatório de vendas de cada loja que controlamos.</p>

<p>Faturamento:</p>
{faturamento.to_html()}

<p>Quantidade vendida:</p>
{Quantidade.to_html()}

<p>ticket médio dos produtos(faturamento por Quantidade) em cada loja:</p>
{ticket_medio.to_html()}

<p>Qualquer dúvida estou a disposição.</p>

<p>Att.,</p>

<p>Diogo</p>
'''

mail.Send()

print('email enviado')