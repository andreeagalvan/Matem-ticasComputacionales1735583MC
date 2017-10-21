Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from heapq import heappop, heappush
>>> def flatten(L):
    while len(L) > 0:
        yield L[0]
        L = L[1]

        
>>> class Grafo:
 
    def __init__(self):
        self.V = set() 
        self.E = dict()
        self.vecinos = dict() 
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: 
            self.vecinos[v] = set() 
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso 
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

    def shortest(self, v): 
        q = [(0, v, ())] 
        dist = dict() 
        visited = set() 
        while len(q) > 0: 
            (l, u, p) = heappop(q)
            if u not in visited: 
                visited.add(u) 
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	
            p = (u, p) 
            for n in self.vecinos[u]: 
                if n not in visited: 
                    el = self.E[(u,n)] 
                    heappush(q, (l + el, n, p))
        return dist

>>> g=Grafo()
>>> g.conecta('a','b',1)
>>>g.conecta('a','c', 2)
>>>g.conecta('a','d', 3)
>>>g.conecta('a','e', 5)
>>>g.conecta('b','c', 1)
>>>g.conecta('b','d', 4)
>>>g.conecta('b','e', 1)
>>>g.conecta('c','d', 2)
>>>g.conecta('c','e', 1)
>>>g.conecta('d','e', 3)
>>>print(g.shortest('a'))
{'a': (0, 'a', ['a']), 'b': (1, 'b', ['a', 'b']), 'c': (2, 'c', ['a', 'c']), 'e': (2, 'e', ['a', 'b', 'e']), 'd': (3, 'd', ['a', 'd'])}