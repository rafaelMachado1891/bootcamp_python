from functools import wraps

from functools import wraps

def validar_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError:
                print("Erro: valor inválido. Tente novamente.")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
    return wrapper