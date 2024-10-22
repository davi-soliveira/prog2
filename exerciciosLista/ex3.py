

"""
Outro metodo de fazer o calculo, mais rapido e com menos linha e menos repetição
def media(nota):
    lst = []
    for i in nota:
        lst.append(i)

    return sum(lst)/len(lst) 
"""

def media(nota):
    lst = []
    res = 0
    for i in nota:
        lst.append(i)
    for j in lst:
        res += j
        

    return res / len(lst)


    

def main():
    nota=[]
    for i in range(4):
        valor = float(input(f"Digite a nota {i+1}: "))
        nota.append(valor)
    print(media(nota))
    



if __name__ == "__main__":
    main()