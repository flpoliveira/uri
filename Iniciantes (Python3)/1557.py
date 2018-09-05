while(True):
    n = int(input())
    if(n == 0):
        break

    matrix = []
    for i in range(n):
        line = []
        if(i == 0 or i == 1):
            k = 2
        else:
            k = k * 2
        aux = k
        for j in range(n):
            if(i == 0 and j == 0):
                line.append(1)
            else:
                line.append(aux)
                aux = aux * 2
        matrix.append(line)
    T = len(str(matrix[n-1][n-1]))

    for i in matrix:
        for j in range(n):
            if(j < (n-1)):
                print('{:{}}'.format(i[j], T), end=' ')
            else:
                print('{:{}}'.format(i[j], T))
    print()