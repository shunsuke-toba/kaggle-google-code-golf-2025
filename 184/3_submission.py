from itertools import*
p=lambda g,f=lambda g:[*zip(*(map(max,*v)for k,v in groupby(g,any)if k))]:f(f(g))