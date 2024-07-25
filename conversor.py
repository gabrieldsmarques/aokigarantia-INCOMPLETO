import pandas, openpyxl

colunas= [4, 6, 9] ##puxando só as colunas necessárias pra geração da nota

##convertendo o excel pra csv pra facilitar a manipulação dos dados
tabela = pandas.read_excel('sucateamento.xlsx', usecols= colunas, engine='openpyxl')
tabela.to_csv('sucateamento.csv', index=False)