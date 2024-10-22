def reverso(numero):
    lst = []
    for j in numero:
        if lst == []:
            lst.append(j)
        if j > lst[0]:
            lst.insert(0,j)
    return lst

def main():
    num=[]
    for i in range(10):
        num.append(i)
    print(reverso(num))

if __name__ == "__main__":
    main()