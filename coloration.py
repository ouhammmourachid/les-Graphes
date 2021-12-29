import numpy as np
def coloration(M):
    pour_ordonee=[sum(i) for i in M]
    M=np.array(M)[np.argsort(pour_ordonee)[::-1]]
    k=0
    B=[i for i in range(len(M))]
    deja_colorer=[]
    while B!=[]:
        k+=1
        colorer_par_k=[]
        while B!=[]:
            colorer_par_k=[]
            colorer_par_k+=[B[0]]
            deja_colorer+=[B[0]]
            del B[0]
            C=[]
            for i in B:
                for j in colorer_par_k:
                    if M[i,j]!=0:
                        C+=[i]
            B=C[:]
        B=[i for i in range(len(M)) if i not in deja_colorer]
    return k

