
#1 importar a base de dados

import pandas as pd
import plotly.express as px


tabela = pd.read_csv("telecom_users.csv")

#2 visualizar a base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)
#caso voce queira excluir mais de uma coluna 
# tabela = tabela.drop(["Unnamed: 0", "IDCliente","Aposentado"], axis=1)
# print(tabela)

#axis = 1 exclui a coluna
#axix = 0 exclui a linha 




#3 passo tratamento de dados


#3 passo tratamento de dados

#comando para converter tabelas para valor numerico
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

#valores vazios
#colunas vazias/Nan -> excluir
tabela = tabela.dropna(how="all", axis=1)


#linhas com valor vazio/NaN -> excluir
tabela = tabela.dropna(how="any", axis=0)

print(tabela)
#4 analise simples -> entender como estao acontecendo os cancelamentos


print (tabela["Churn"].value_counts())


print (tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))


#cria o grafico

for coluna in tabela.columns:
       print(coluna)
       grafico = px.histogram(tabela, x=coluna, color="Churn")

       grafico.show()
#exibe o grafico

