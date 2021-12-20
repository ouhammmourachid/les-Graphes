
# we import numpy library.

import numpy as np

# the definition of our function.

def niveaux_graphe(M):

    M=np.array(M)

    # we create the list that will contine our niveaux of graphe and we create X(0)

    S=[[] for i in range(len(M))]

    # we create the p list to store all the sommet that we already traite .
    
    p=[i for i in range(len(M)) if list(M[i])==[0 for i in range(len(M))] ]
    c=0
    S[c]=p.copy()
    x=[1]
    while x!=[]:
        for k in S[c]:
            M[:,k]=-M[:,k]
        c=c+1
        x=[i for i in range(len(M)) if 1 not in M[i] and i not in p]
        S[c]=x
        p+=x
    return [ [ i+1 for i in L] for L in S]



M=[[0,1,0,1,0],[0,0,1,1,0],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,0]]
print(niveaux_graphe(M))