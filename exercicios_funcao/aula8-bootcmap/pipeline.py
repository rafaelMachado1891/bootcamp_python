import pandas as pd
import os
import glob

def ler_e_concatenar_arquivos_json(pasta:str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index= True)
    return df_total

def calcular_kpis_de_negocio(df: pd.DataFrame) -> pd.DataFrame:
    df['total'] = df['Quantidade'] * df['Venda']
    return df

def carregar_dataframe_em_arquivos(df: pd.DataFrame, formato: list):
    for i in formato:
        if i == "csv":
            df.to_csv('dados.csv', index=False)
        if i == "parquet":
            df.to_parquet('dados.parquet', index= False)

def pipeline_completa_etl_json(path_do_arquivo: str, formato_de_saida: list):
    """
    pipeline que lê, concatena, calcula os KPIS e salva em arquivo csv ou parquet ou ambos os formatos.
    path_do_arquivo: informe o caminho dos seus arquivos JSON.
    formato_de_saida: "informe o tipo de saida desejado exemplo ['parquet']

    """
    dados= ler_e_concatenar_arquivos_json(path_do_arquivo)
    df = calcular_kpis_de_negocio(dados)
    carregar_dataframe_em_arquivos(df,formato_de_saida)


