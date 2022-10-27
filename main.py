def simplify(C : list) -> list:  
    '''
        Receive a list as parameter, and simplify by removing atomic formulas if possible,
        until theres no atomic formula left.
        
        Parameters
        ----------
        C : list
            A list where each element is a formula.
            
        Return
        -------
        C -> A list containing the remaining formulas.
    '''
    print("C to simplify: ", C) 
    i = 0
    while i < len(C):
        if len(C[i]) == 1:
            j = 0
            aux = C.pop(i)[0]
            while j < len(C):
                if aux in C[j]:
                    C.pop(j)
                    j-=1
                    i = 0
                elif -aux in C[j]:
                    C[j].pop(C[j].index(-aux))
                    i = 0
                j+=1
        else: i+=1
    return C


def twoSat(C : list):
    '''
        Receives a set of formula and check the satisfiability of the set.
        
        Parameters
        ----------
        C : list
            A list C that contains all formulas.
        
        Return
        ------
        True
            If the formula set is satisfiable.
        False
            If the formula set is unsatisfiable.
    '''
    C = simplify(C)
    print("C in twoSat:", C)
    
    while [] not in C and C != []:
        aux = C[0][0]
        CF = C
        CF.append([aux])
        CF = simplify(CF)
        if [] in CF:
            CF = C
            CF.append([-aux])
            CF = simplify(CF)
        else: 
            C = CF
    if [] in C: return False
    else: return True
           
def main():
    file = open("elems.txt", "r")
    fSize = len(file.readlines())
    i = 0
    lista = []
    file.seek(0)
    while i < fSize:
        lista.append(list(map(int, file.readline().split())))
        i+=1
    print(twoSat(lista))           

if __name__ == "__main__":
    main()