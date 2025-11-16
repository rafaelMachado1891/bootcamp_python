from pipeline import pipeline_completa_etl_json

pasta = 'C:/Users/rafad/Documents/Repositorios_Git/bootcamp_python/exercicios_funcao/aula8-bootcmap/data'
formato = ["parquet", "csv"]

pipeline_completa_etl_json(pasta, formato)