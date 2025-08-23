def p(g):
 W=len(g);f=sum(g,[])
 (a,b),*_,(c,d)=[divmod(i,W)for i,v in enumerate(f)if v==4]
 s=[(u,v)for i,w in enumerate(f)if w*(w-4)and min((u:=i//W)-a,c-u,(v:=i%W)-b,d-v)<0]
 S,J=map(min,zip(*s))
 o=[r[b:d+1]for r in g[a:c+1]]
 f=next(g[i][J]for i,j in s if j==J)==g[a+1][d]
 for k in range(~a+c):r=g[S+k][J:J+~b+d];o[k+1][1:-1]=r[::-1]if f else r
 return o
