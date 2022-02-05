import numpy as np
def coloration(M):
    pour_ordonee=[sum(i) for i in M]
    B= [ i for i in np.argsort(pour_ordonee)[::-1] ]
    print(B)
    k=0
    ordoner_ordre_croisant = B.copy()
    deja_colorer = []
    while B!=[]:
        k+=1
        colorer_par_k = []
        while B != []:
            colorer_par_k += [B[0]]
            deja_colorer += [B[0]]
            del B[0]
            C=[]
            for i in B:
                if sum([ M[i][j] for j in colorer_par_k ]) == 0:
                    C += [i]
            B=C[:]
        print(colorer_par_k)
        B=[i for i in ordoner_ordre_croisant if i not in deja_colorer]
    return k
