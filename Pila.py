class Pila:
	def __init__(self):
		self.pila = []
	
	def obtener(self):
		return self.pila.pop()
	def meter(self,e):
		self.pila.append(e)
		return len(self.pila)
	@property
	def longitud(self):
		return len(self.pila)