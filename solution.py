import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 783077646 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    _, res = w.ztest(x, value=500, alternative='larger')
    return res <= 0.1 # Ваш ответ, True или False
