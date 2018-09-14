while True:
	try:
		n = int(input())
		entrada = input().split(" ")
		lista = []
		for x in range(n):
			lista.append(int(entrada[x]))

		soma1 = 0
		soma2 = sum(lista)
		dif = 9999999999
		for x in lista:
			soma1 = soma1 + x
			soma2 = soma2 - x

			if(abs(soma1 - soma2) == 0):
				dif = 0
				break
			elif(abs(soma1 - soma2) < dif):
			 	dif = abs(soma1 - soma2)
			
		print(dif)
	except:
		break