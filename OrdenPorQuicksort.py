contador=0
def OrdenPorQuicksort(arr):
	global contador
	if len(arr)<=1:
		return arr
	p=arr.pop(0)
	menores,mayores=[],[]	
	for j in arr:
		contador+=1
		if j<=p:
			menores.append(j)	
		else:
			mayores.append(j)
	return quicksort(menores) + [p] + quicksort(mayores)