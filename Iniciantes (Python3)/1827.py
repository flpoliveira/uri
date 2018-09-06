while (True):
    try:
        n = int(input())

        mid = int(n / 2)
        tam = int(n / 3)
        tamLimit = n - tam
        matrix = []
        for i in range(n):
            line = []
            for j in range(n):
                if (i == mid and j == mid):
                    line.append(4)
                elif (i >= tam and i < tamLimit and j >= tam and j < tamLimit):
                    line.append(1)
                elif (i == j):
                    line.append(2)
                elif (j == (n - 1 - i)):
                    line.append(3)
                else:
                    line.append(0)
            matrix.append(line)

        output = ''
        for line in matrix:
            for j in line:
                output = output + str(j)
            output = output+ '\n'
        print(output)

    except:
        break