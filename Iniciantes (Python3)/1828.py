n = int(input())
for i in range(n):
    a,b = input().split(" ")
    if(a == b):
        print("Caso #%i: De novo!" % (i+1))
    else:
        lista = ["tesoura", "papel", "pedra", "lagarto", "Spock", "tesoura", "lagarto", "papel", "Spock", "pedra"]
        lista2 = ["papel", "pedra", "lagarto", "Spock", "tesoura", "lagarto", "papel", "Spock", "pedra", "tesoura"]

        for j in range(10):
            if(a == lista[j] and b == lista2[j]):
                print("Caso #%i: Bazinga!" % (i+1))
                break
            elif(b == lista[j] and a == lista2[j]):
                print("Caso #%i: Raj trapaceou!" % (i+1))
                break