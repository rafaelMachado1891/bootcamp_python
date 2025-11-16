from modulo import ler_arquivo_csv, calcular_coluna_total_vendas, calcular_soma_total_vendas, calcular_total_de_vendas_por_categoria

caminho = "C:\\Users\\rafad\\Documents\\Repositorios_Git\\bootcamp_python\\exercicios_funcao\\vendas.csv"

dados = ler_arquivo_csv(caminho)

resultado = calcular_coluna_total_vendas(dados)

valor_vendas = calcular_soma_total_vendas(resultado)

valor_vendas_por_categoria = calcular_total_de_vendas_por_categoria(resultado)

print(valor_vendas_por_categoria)

print(f'o valor total de vendas é {valor_vendas}')


