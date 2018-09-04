for x in range ((int(input()))):
	entrada = input().split(" ")
	A = int(entrada[0])
	B = int(entrada[1])
	pA = float(entrada[2])
	pB = float(entrada[3])

	i = 0

	while(A <= B and i < 101):
		i += 1
		A += int(pA*A/100)
		B += int(pB*B/100)

	if(i > 100):
		print("Mais de 1 seculo.")
	else:
		print(str(i) + " anos.")