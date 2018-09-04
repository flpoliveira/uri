par = []
impar = []
for x in range(15):
	n = int(input())
	if(n % 2 == 0):
		par.append(n)
	else:
		impar.append(n)

	if(len(par) >= 5):
		for i in range(len(par)):
			print("par[%i] = %i" % (i, par[i]))
		par = []
	if(len(impar) >= 5):
		for i in range(len(impar)):
			print("impar[%i] = %i" %(i, impar[i]))
		impar = []
for i in range(len(impar)):
	print("impar[%i] = %i" % (i, impar[i]))
for i in range(len(par)):
	print("par[%i] = %i" % (i, par[i]))