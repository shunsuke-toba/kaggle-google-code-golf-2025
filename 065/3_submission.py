def p(g):
 n=len(g)//2;b=g[0][0],g[0][-1],g[-1][0],g[-1][-1]
 return next((a for y in(0,n+1)for x in(0,n+1)for a in([r[x:x+n]for r in g[y:y+n]],)if{*sum(a,[])}-{a[0][0]}),[[min(b,key=b.count)]])
