import itertools as I
p=lambda g,f=lambda g:[*zip(*(map(max,*v)for k,v in I.groupby(g,any)if k))]:f(f(g))