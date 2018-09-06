entrada = input().split(" ")
a = int(entrada[0])
b = int(entrada[1])

r = abs(a % b)

q = int((a-r)/b)

print("%d %d" % (q, r))

https://www.udesc.br/arquivos/cct/id_cpmenu/1208/Programac_a_o_Computacao_15360943543172_1208.pdf