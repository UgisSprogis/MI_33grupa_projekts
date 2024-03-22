from heiristiska_funkcija import *


max_limenis = sp.virsotnes[len(sp.virsotnes)-1].limenis
atk_virsotnes=[]
for x in sp.virsotnes:
    atk_virsotnes.append([x.id,x.skaitlis,x.speletajs1,x.speletajs2,x.limenis])

def berni(pasreizeja_virsotne):
    berni = []
    a = []
    a = sp.loki.get(pasreizeja_virsotne[0])
    for x in a:
        for y in atk_virsotnes:
            if x == y[0]:
                berni.append(y)
    return berni


def alphabeta(virs, alpha, beta):
    if virs[4] == max_limenis:
        return virs[4] + virs[2] - virs[3]
    next_states = berni(virs)
    if not isinstance(next_states, list):
        next_states = [next_states]
    if (virs[4] % 2) == 0:
        value = float('-inf')
        for state in next_states:
            value = max(alphabeta(state, alpha, beta) for state in next_states)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    elif (virs[4] % 2) == 1:
        value = float('inf')
        for state in next_states:
            value = min(alphabeta(state, alpha, beta) for state in next_states)
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value



result = alphabeta(atk_virsotnes[0], float('-inf'), float('inf'))
print(result)


