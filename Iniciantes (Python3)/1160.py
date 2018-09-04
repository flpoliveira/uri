for x in range ((int(input()))):
	entrada = input().split(" ")
	A = float(entrada[0])
	B = float(entrada[1])
	pA = float(entrada[2])
	pB = float(entrada[3])

	i = 0

	while(A <= B):
		i += 1
		A += int((pA/100) * A)
		B += int((pB/100) * B)

	if(i > 100):
		print("Mais de 1 seculo.")
	else:
		print(str(i) + " anos.")