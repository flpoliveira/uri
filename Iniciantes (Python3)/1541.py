while(True):
    entrada = input().split(" ")
    if(int(entrada[0]) == 0):
        break
    A = int(entrada[0])
    B = int(entrada[1])
    C = int(entrada[2])

    output = int(pow(((A*B *100)/C), (1/2)));
    print(output)