def p(g):
 _,q,x,b=max(((q:=g[y:y+a])and (max(max(r[x:x+b])for r in q)<1)*a*b,q,x,b)for y in range(len(g))for x in range(len(g[0]))for a in range(2,len(g)-y+1)for b in range(2,len(g[0])-x+1))
 for r in q:r[x:x+b]=[6]*b
 return g