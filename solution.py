from scipy import stats
import numpy as np

chat_id = 341299061 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    p = (x_success + y_success) / (x_cnt + y_cnt)
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    z_stat = (p1 - p2) / np.sqrt(p * (1 - p) * ((1 / x_cnt) + (1 / y_cnt)))
    p_value = stats.norm.sf(abs(z_stat)) * 2
    return p_value < 0.02
