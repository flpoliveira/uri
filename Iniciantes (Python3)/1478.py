while(1):

    n = int(input())
    if(n == 0):
        break
    matrix = []
    for i in range(1, (n+1)):
        line = []
        value = i
        for j in range(n):
            line.append(abs(value))
            if(value == 1):
                value -= 3
            else:
                value -= 1
        matrix.append(line)


    # output = ''
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

