def primo(n):
	for i in range(2,round(n**0.5)):
		if (n%i)==0:
			return('no')
	return ('si')


