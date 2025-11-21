import pandas as pd

class ProcessadorCSV:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.df = None
        
    def carregar_csv(self):
        self.df = pd.read_csv(self.arquivo_csv)
        
    def remover_celula_vazias(self):
        self.df = self.df.dropna()
        
    def filtar_por_categoria(self, categoria):
        self.df = self.df[self.df['categoria'] == categoria]
        
    def processar(self, categoria):
        self.carregar_csv()
        self.remover_celula_vazias()
        self.filtar_por_categoria("xpto")
        
        return self.df
    
    
arquivo_csv = './exemplo.csv' 
filtro_aplicado = 'SP'  # estado que você quer filtrar

processador = ProcessadorCSV(arquivo_csv)
df_filtrado = processador.processar(filtro_aplicado)

print(df_filtrado)