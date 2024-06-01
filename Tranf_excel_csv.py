import pandas as pd

caminho_arquivo_excel = r"C:\Users\heloi\OneDrive\Área de Trabalho\Prog\Excel_Csv\Dados\Grafos_Dados.xlsx" #necessário trocar para o caminho que foi salvo

dataframe = pd.read_excel(caminho_arquivo_excel, engine='openpyxl')

caminho_arquivo_csv = r"C:\Users\heloi\OneDrive\Área de Trabalho\Prog\Excel_Csv\Dados\Grafos_Dados.csv" #necessário trocar para o caminho que quer salvar

dataframe.to_csv(caminho_arquivo_csv, index=False)

leitura_csv = pd.read_csv(caminho_arquivo_csv)

filmes_separados = leitura_csv['Filmes'].str.split(',', expand=True)

filmes_separados.name = 'Filmes'

dataframe = leitura_csv.drop('Filmes', axis=1).join(filmes_separados)

print(dataframe)