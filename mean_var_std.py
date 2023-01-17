import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    x = [list[i:i + 3] for i in range(0, len(list), 3)]
    ls = np.array(x)
    medias = [ls.mean(axis=0).tolist(), ls.mean(axis=1).tolist(), ls.mean()]
    variances = [ls.var(axis=0).tolist(), ls.var(axis=1).tolist(), ls.var()]
    deviations = [ls.std(axis=0).tolist(), ls.std(axis=1).tolist(), ls.std()]
    maximos = [ls.max(axis=0).tolist(), ls.max(axis=1).tolist(), ls.max()]
    minimos = [ls.min(axis=0).tolist(), ls.min(axis=1).tolist(), ls.min()]
    sumatorios = [ls.sum(axis=0).tolist(), ls.sum(axis=1).tolist(), ls.sum()]
    resultado = {
        'mean': medias, 
        'variance': variances, 
        'standard deviation': deviations,
        'max': maximos,
        'min': minimos,
        'sum': sumatorios
        }
    return resultado
