contador=0
def OrdenPorSeleccion(a):
	global contador
	for i in range(0,len(a)-1):
		val=i
		for j in range(i+1,len(a)):
			contador=contador+1
			if a[j]<a[val]:
				val = j
				if val !=i:
					aux=a[i]
					a[i]=a[val]
					a[val]=aux
	return contador