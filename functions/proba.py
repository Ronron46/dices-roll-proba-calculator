def proba(count, target, res_min):
    aux=0
    for i in range(len(count) - target + res_min):
        aux += count[i + target - res_min]
    return aux/sum(count)
