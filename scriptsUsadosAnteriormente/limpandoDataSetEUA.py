import pandas as pd

caminho = r"C:\Users\dorfb\OneDrive\Documentos\TCC\datasets\ibtracs_USA.csv"

# na_values trata espaços em branco como nulos
df = pd.read_csv(caminho, low_memory=False, na_values=[' ', ''])

print(f"Colunas antes: {df.shape[1]}")

# Remove colunas com 80% ou mais de valores vazios
limite = 0.80
df = df.dropna(axis=1, thresh=int(len(df) * (1 - limite)))

print(f"Colunas depois: {df.shape[1]}")
print(f"Colunas restantes: {df.columns.tolist()}")

df.to_csv(r"C:\Users\dorfb\OneDrive\Documentos\TCC\datasets\ibtracs_USA_limpo.csv", index=False)
print("Arquivo salvo: ibtracs_USA_limpo.csv")