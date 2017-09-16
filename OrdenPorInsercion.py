contador=0

def OrdenPorInsercion(arr):

	global contador
	for indice in range(1,len(arr)):

		valor=arr[indice]

		i=indice-1

		while i>=0:

			contador+=1

			if valor<arr[i]:

				arr[i+1]=arr[i]

				arr[i]=valor

				i-=1

			else:

				break

	return arr