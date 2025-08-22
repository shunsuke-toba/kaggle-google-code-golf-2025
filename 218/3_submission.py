from itertools import groupby as g
p=lambda m:(m:=[r for r,_ in g(m) if any(r)],m:=list(zip(*m)),m:=[r for r,_ in g(m) if any(r)],list(map(list,zip(*m))))[-1]
