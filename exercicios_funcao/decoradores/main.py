import time
from functools import wraps
from fastapi import FastAPI
from utils import validar_input

# app = FastAPI()

# def minha_funcao_decorada(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("essa é a minha funcao decorada")
#         return func(*args, **kwargs)
#     return wrapper

# def medidor_de_tempo(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         t_inicial = time.time()
#         res = func(*args, **kwargs)
#         t_final = time.time()
#         print(f"A função levou {t_final - t_inicial:.6f} segundos para rodar")
#         return res
#     return wrapper

# @app.get("/funcao_soma")
# @medidor_de_tempo
# @minha_funcao_decorada
# def funcao_soma(x: int, y: int) -> dict:
#     resultado = x + y
#     return {"resultado": resultado}


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

@validar_input
def calcular_potencia() ->int:
    base = int(input('digite o valor da base: '))
    expoente = int(input('digite o valor do expoente: '))
    resultado = base ** expoente
    return resultado


resultado = calcular_potencia()

print(resultado)