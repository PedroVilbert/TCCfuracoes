import pandas as pd

# Carrega o dataset pulando a linha 1 (que contém unidades, não dados)
df = pd.read_csv(
    r"C:\Users\dorfb\OneDrive\Documentos\TCC\ibtracs.ALL.list.v04r01.csv",
    skiprows=[1],
    low_memory=False
)

# ── Filtro 1: registros cuja agência WMO responsável é americana ──────────────
# hurdat_atl = HURDAT2 Atlântico (NHC/NOAA)
# hurdat_epa = HURDAT2 Pacífico Leste (NHC/NOAA)
agencias_usa_wmo = ["hurdat_atl", "hurdat_epa"]

df_usa = df[df["WMO_AGENCY"].str.strip().isin(agencias_usa_wmo)].copy()

# ── Filtro 2 (alternativo/complementar): registros com dados da USA_AGENCY ───
# Descomente abaixo se quiser incluir também registros onde a agência americana
# contribuiu com dados, mesmo que outra agência seja a WMO responsável.
#
# agencias_usa = ["hurdat_atl", "hurdat_epa", "atcf", "cphc", "jtwc_ep", "jtwc_cp"]
# df_usa = df[df["USA_AGENCY"].str.strip().isin(agencias_usa)].copy()

# ── Resultado ─────────────────────────────────────────────────────────────────
print(f"Total de registros no dataset original : {len(df):,}")
print(f"Registros das estações americanas       : {len(df_usa):,}")
print(f"Agências presentes no recorte           : {df_usa['WMO_AGENCY'].unique()}")

# Salva o recorte
df_usa.to_csv("ibtracs_USA.csv", index=False)
print("Arquivo salvo: ibtracs_USA.csv")