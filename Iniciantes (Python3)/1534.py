# a00 a01 a02 a03 a04
# a10 a11 a12 a13 a14
# a20 a21 a22 a23 a24
# a30 a31 a32 a33 a34
# a40 a41 a42 a43 a44

while True:
    try:
        n = int(input())
        output = ''
        for i in range(n):
            for j in range(n):
                if(j == i):
                    if((n%2 == 1) and (j == (n-1)/2)):
                        output = output + "2"
                    else:
                        output = output + "1"
                elif((j + i) == (n-1)):
                    output = output + "2"
                else:
                    output = output + "3"

            if(i != (n-1)):
                output = output + "\n"
        print(output)

    except:
        break