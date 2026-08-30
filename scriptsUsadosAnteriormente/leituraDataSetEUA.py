import pandas as pd
import os

os.system("cls")

caminho = r"C:\Users\dorfb\OneDrive\Documentos\TCC\datasets\ibtracs_USA_formatado.csv"

cols = ['ID', 'DATA_HORA', 'LATITUDE', 'LONGITUDE', 'ESCALA_SAFFIR_SIMPSON']

df = pd.read_csv(caminho, low_memory=False, usecols=cols, parse_dates=['DATA_HORA'])
# df = pd.read_csv(caminho, low_memory=False, parse_dates=['DATA_HORA'])

print(f"Total de registros : {len(df):,}")
print(f"Período            : {df['DATA_HORA'].min()} até {df['DATA_HORA'].max()}")
print(f"Total de furacões  : {df['ID'].nunique()}")
print()
print(df.head(60))

# Lê só o cabeçalho, sem carregar os dados
# colunas = pd.read_csv(caminho, nrows=0).columns.tolist()
# print(colunas)