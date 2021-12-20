
# we import library numpy and random

import numpy as np
import random

# we had already code this part but remmber the use of global for A varible.



def sans_circuit(M):
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    global A , dic
    A=M
    dic=[i for i in range(len(A))]
    while list(np.zeros(len(A))) in A:
        illiminer=[]
        for i in range(len(A)):
            if list(np.zeros(len(A)))==A[i]:
                illiminer+=[i]
                dic.remove(i)
        A=[[A[i][j] for i in range(len(A)) if i not in illiminer] for j in range(len(A)) if j not in illiminer]
    a=(A==[])
    A=np.array(A)
    if a:return True
    return False


# here the difinition of the function that search for a circuit and return one.

def trouver_circuit(M):

    # here we cheack if the graphe contine a ciruit it will exicute the instraction in side if
    # other wise it will return an empty list

    if not sans_circuit(M):

        # here we use the global varible in function sans circuit and choose randomly a sommet.


        v=random.choices([i for i in range(len(A))])
        S=v

        # we create a boulien varible 

        a=False


        # 


        while not a:

            # we choose randomly from all suiveur except those who already exist in S.

            k=random.choices([i for i in range(len(A)) if A[v,i]==1 and i not in S])
            S+=k
            v=k
            
            # here we cheack if there is a "successeur" of v in S 
            # here we use numpy library.

            for j in S:
                if (A[v]==1).reshape((len(A),1))[j]==True:
                    a=True
                    break
                else:
                    a=False
        # the end of the boocle while.

        # here we store nomber that refer to the start of our circuit in S.

        n=list(np.array(S)==j).index(True)

        # here we successfuly had create our circuit.
        # and the if is used some case if len(A)!=len(M)

        b=[dic[i] for i in (S+[j])[n:]]

        if len(dic)!=len(M):
            b.reverse()

        # the return of the fuctiion

        return np.array(b)+np.ones((len(b),))
    return []

# if we want more circuit we can use .

def more_circuit(M):
    for i in range(20):
        random.seed()
        print(trouver_circuit(M))



# some exemples
Q=[[0,0,0,0,1],[0,0,0,0,0],[1,0,0,0,0],[0,1,1,0,0],[0,1,1,1,0]]
M=[[0,1,0,0,0,0],[0,0,0,1,1,0],[0,0,0,0,0,0],[1,0,0,1,1,0],[0,0,0,1,0,1],[0,0,1,0,0,0]]
N=[[0,1,0,0,0],[1,0,1,0,0],[0,0,0,1,1],[0,0,0,0,1],[1,0,0,0,0]]
print(trouver_circuit(Q))