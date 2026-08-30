import pandas as pd

caminho_entrada = r"C:\Users\dorfb\OneDrive\Documentos\TCC\datasets\ibtracs_USA_limpo.csv"
caminho_saida   = r"C:\Users\dorfb\OneDrive\Documentos\TCC\datasets\ibtracs_USA_formatado.csv"

df = pd.read_csv(caminho_entrada, low_memory=False, na_values=[' ', ''])

# ── 1. ISO_TIME → datetime ────────────────────────────────────────────────────
df['ISO_TIME'] = pd.to_datetime(df['ISO_TIME'])

# ── 2. Colunas categóricas com mapeamento legível ────────────────────────────
df['NATURE'] = df['NATURE'].map({
    'TS': 'Tropical',
    'ET': 'Extratropical',
    'MX': 'Misto',
    'SS': 'Subtropical',
    'DS': 'Distúrbio'
})

df['USA_STATUS'] = df['USA_STATUS'].map({
    'HU': 'Furacão',
    'TS': 'Tempestade Tropical',
    'TD': 'Depressão Tropical',
    'EX': 'Extratropical',
    'SS': 'Tempestade Subtropical',
    'SD': 'Depressão Subtropical',
    'LO': 'Baixa Pressão',
    'DB': 'Distúrbio',
    'WV': 'Onda Tropical'
})

df['WMO_AGENCY'] = df['WMO_AGENCY'].map({
    'hurdat_atl': 'HURDAT Atlântico',
    'hurdat_epa': 'HURDAT Pacífico Leste'
})

df['SUBBASIN'] = df['SUBBASIN'].map({
    'GM': 'Golfo do México',
    'CS': 'Caribe',
    'CP': 'Pacífico Central',
    'MM': 'Mar do México',
    'NA': 'Atlântico Norte'
})

# ── 3. Renomear colunas para nomes mais claros ────────────────────────────────
df = df.rename(columns={
    'SID'         : 'ID',
    'SEASON'      : 'ANO',
    'NUMBER'      : 'NUMERO',
    'NAME'        : 'NOME',
    'ISO_TIME'    : 'DATA_HORA',
    'NATURE'      : 'NATUREZA',
    'LAT'         : 'LATITUDE',
    'LON'         : 'LONGITUDE',
    'WMO_WIND'    : 'VENTO_WMO_KTS',
    'WMO_PRES'    : 'PRESSAO_WMO_MB',
    'WMO_AGENCY'  : 'AGENCIA',
    'TRACK_TYPE'  : 'TIPO_TRAJETORIA',
    'DIST2LAND'   : 'DIST_TERRA_KM',
    'LANDFALL'    : 'DIST_LANDFALL_KM',
    'USA_AGENCY'  : 'AGENCIA_USA',
    'USA_ATCF_ID' : 'ID_ATCF',
    'USA_LAT'     : 'LATITUDE_USA',
    'USA_LON'     : 'LONGITUDE_USA',
    'USA_STATUS'  : 'CATEGORIA',
    'USA_WIND'    : 'VENTO_USA_KTS',
    'USA_PRES'    : 'PRESSAO_USA_MB',
    'USA_SSHS'    : 'ESCALA_SAFFIR_SIMPSON',
    'USA_POCI'    : 'PRESSAO_EXTERNA_MB',
    'USA_ROCI'    : 'RAIO_PRESSAO_EXTERNA_NM',
    'USA_RMW'     : 'RAIO_VENTO_MAX_NM',
    'STORM_SPEED' : 'VELOCIDADE_TEMPESTADE_KTS',
    'STORM_DIR'   : 'DIRECAO_TEMPESTADE_GRAUS',
})

# ── 4. Converter ventos de nós (kts) para km/h ───────────────────────────────
df['VENTO_WMO_KMH'] = (df['VENTO_WMO_KTS'] * 1.852).round(1)
df['VENTO_USA_KMH'] = (df['VENTO_USA_KTS'] * 1.852).round(1)

# ── 5. Resultado ─────────────────────────────────────────────────────────────
print(f"Shape final: {df.shape}")
print(df.head(3).to_string())

df.to_csv(caminho_saida, index=False)
print(f"\nArquivo salvo: {caminho_saida}")