
# we import library numpy 

import numpy as np  

# here the definition of our function that return False if there is a circuit i M and True other wise.

def sans_circuit(M):

    # here we make A and dic a global variable his use will not appear in this function but
    # it will be very useful in the function trouve_circuit.

    global A , dic
    A=M

    #  we fill our list dic with all the sommet .

    dic=[i for i in range(len(A))]

    # the condition of the while boocl is A still contine a line fill the all 0. 

    while list(np.zeros(len(A))) in A:

        # in this part we store all the line that still contine just 0 .
        # and also we remove them from the dic list.

        illiminer=[]
        for i in range(len(A)):
            if list(np.zeros(len(A)))==A[i]:
                illiminer+=[i]
                dic.remove(i)

        # here we remove all the line and colome  in A that existe in illiminer.

        A=[[A[i][j] for i in range(len(A)) if i not in illiminer] for j in range(len(A)) if j not in illiminer]

    
    # after all that we check if A equale [] we return True other wise we return False.

    a=(A==[])

    A=np.array(A)

    if a:return True

    return False
