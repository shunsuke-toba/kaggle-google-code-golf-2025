def p(g):
 t=*zip(*g),
 m=0,*map(min,t),0
 return any(m)and[[m[x+1]or m[x]*(m[x]in r[x:])or m[x+2]*(m[x+2]in r[:x+1])for x in range(len(r))]for r in g]or[*zip(*p(t))]