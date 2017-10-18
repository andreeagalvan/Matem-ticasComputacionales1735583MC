cnt=0
def fibonacci(n):
	global cnt
	cnt+=1
	if n==0 or n==1:
		return(1)
	else:
		return fibonacci(n-2)+fibonacci(n-1)