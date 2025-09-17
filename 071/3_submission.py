def p(g,a=0):
 return[[v and(a or(t:=i-r[::-1].index(v),a:=v))and(v*(v==a)or r[~i+t]) for i,v in enumerate(r)]for r in g]