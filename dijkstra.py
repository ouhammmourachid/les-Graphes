import numpy as np
U=[['A','B',7],['A','C',1],['B','D',4],['B','F',1],['C','B',5],['C','E',2],['C','F',7],['E','B',2],['E','D',5],['F','E',3]]
X=['A','B','C','D','E','F']
def Connect(U,X,start,end):
    if end==start: return True
    allready=[]
    file=[]
    a=False
    while file!=X:
        s=[i[1] for i in U if i[0]==start and i[1] not in allready]
        if end in s:
            return True
        file+=s
        if file==[]:
            break
        start=file.pop(0)
        allready+=[start]
    return False

def is_root(X,U,start):
    a=True
    for end in X:
        a=Connect(U,X,start,end)
        if not a:
            break   
    return a
def Dijkstra(X,U,start):
    L=[np.inf for i in range(len(X))]
    P=['-' for i in range(len(X))]
    M=[]
    s=0
    for sommet in X:
        for Ar in U:
            if start==sommet :
                L[s]=0
                P[s]=start
            if Ar[0]==start and Ar[1]==sommet:
                L[s]=Ar[2]
                P[s]=start
                break
        s+=1
    M=[start]
    while len(M)!=len(X):
        X_M=[ X.index(i) for i in X if i not in M]
        min_dis=np.inf
        for i in X_M:
            if L[i]<=min_dis:
                min_dis=L[i]
                x=X[i]
        successeur=[ Ar[1] for Ar in U if Ar[0]==x and Ar[1] not in M]
        for i in X_M:
            for Ar in U:
                if Ar[0:2]==[x,X[i]]:
                    v=Ar[2]
                    break
            if X[i] in successeur and L[i]>min_dis+v:
                L[i]=min_dis+v
                P[i]=x
        M+=[x]
    return L,P,M