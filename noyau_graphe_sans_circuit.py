import numpy as np
def noyau(M):
    Y=[]
    C=[]
    j=M.index([0 for i in range(len(M))])
    Y.append(j)
    B=[j]
    B+=[i for i in range(len(M)) if M[i][j]==1]
    M=np.array(M)
    for b in B:
        M[:,b]=-M[:,b]
    while len(B)!=len(M):
        J=[i for i in range(len(M)) if i not in B and 1 not in M[i]]
        j=J[0]
        Y+=[j]
        C=[i for i in range(len(M)) if i not in B and 1 not in M[i]]
        B+=[i for i in range(len(M)) if i not in B and 1 in M[i] ]
        for c in C:
            M[:,c]=-M[:,c]
        B+=C
    return np.array(Y)+np.ones((len(Y),))

    