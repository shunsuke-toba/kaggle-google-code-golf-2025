def p(g):
 y,x=divmod(sum(g,[]).index(8),len(g[0]));a=[r[x-1:x+2]for r in g[y-1:y+2]];a[1][1]=max({*sum(a,[])}-{8});return a
