import numpy as np

def exist_j(X,S,C,F):
    global exist_i 
    global exist_j
    X_S = (i for i in X if i not in S)
    for j in X_S:
        for i in S:
            if C[i][j] - F[i][j]>0 or F[j][i]>0:
                exist_j = j
                exist_i = i
                return True
    return False


def optimisation_de_flot(X,C,s,p):
    F = [[0 for i in range(len(X))]for j in range(len(X))]
    M = [[] for i in range(len(X))]
    M[s] = [np.inf,np.inf,+1]
    V =0
    S = [s]
    while exist_j(X,S,C,F):
        i = exist_i
        j = exist_j
        if C[i][j] - F[i][j]>0:
            M[j] = [i,min(M[i][1],C[i][j] - F[i][j]),+1]
        else:
            M[j] = [i,min(M[i][1],F[j][i]),-1]
        S.append(j)
        if j==p:
            V += M[p][1]
            break
    if p in S:
        while j != s:
            F[M[j][0]][j] += M[j][2]*M[p][1]
            j = M[j][1]
        F,M,V = optimisation_de_flot(X,C,s,p)
    return F,M,V



