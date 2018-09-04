while(1):

    n = int(input())
    if(n == 0):
        break
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(1)
        matrix.append(line)
    if(n % 2 == 0):
        mid = n/2
    else:
        mid = (n+1) / 2

    value = 1
    left = 0
    right = n-1
    down = n-1
    up = 0
    aux = n
    while(value <= mid):
        aux = left
        while(aux <= right):
            matrix[up][aux] = value
            matrix[down][aux] = value
            aux += 1

        aux = (up+1)

        while(aux < down):
            matrix[aux][left] = value
            matrix[aux][right] = value
            aux+= 1

        value += 1
        up += 1
        down -= 1
        left += 1
        right -= 1
    output = ''
    # for i in range(n):
    #     for j in range(n):
    #         if(j == 0):
    #             output = output + "%3i" % matrix[i][j]
    #         else:
    #             output = output +" %3i" % matrix[i][j]
    #     output = output + '\n'
    # output = output + '\n'
    # print(output)
    for i in range(n):
        tx = ''
        for j in range(n):
            tx += " %3d" % matrix[i][j]
        print(tx[1:])
    print("")

