def ler_arquivo_csv(caminho_arquivo: str) -> list[dict]:
    import csv
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        lista = []
        for i in leitor:
            lista.append(i)
    return lista

def calcular_coluna_total_vendas(dados:list[dict]) -> list[dict]:
    lista = []
    for coluna in dados:
        quantidade = int(coluna.get('Quantidade',0))
        valor = float(coluna.get('Venda',0))
        coluna['total'] = quantidade * valor
        lista.append(coluna)
    return lista

def calcular_total_de_vendas_por_categoria(dados: list[dict]) -> list[dict]:
    totais = {}
    for linha in dados:
        categoria = linha.get('Categoria', 'Sem categoria')
        total = float(linha.get('total', 0))

        if categoria in totais:
            totais[categoria] += total
        else:
            totais[categoria] = total

    lista_resultado = []
    for categoria, soma in totais.items():
        lista_resultado.append({
            "categoria": categoria,
            "total_vendas": soma
        })
    return lista_resultado

def calcular_soma_total_vendas(dados:list[dict]) -> float:
    soma = 0
    for coluna in dados:
        total = float(coluna.get('total',0))
        soma+=total
    return soma

def calcular_soma_total__vandasv2(dados: dict) -> float:
    total=0
    for valor in dados.values():
        total+=valor
    return total