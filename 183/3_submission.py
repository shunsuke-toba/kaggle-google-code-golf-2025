p=lambda g:(n:=len(g)-1,d:=n//2-1,c:=g[::n],e:=enumerate,[[c[i>=d][-(j>=d)]if v>7 else v for j,v in e(r[2:-2])]for i,r in e(g[2:-2])])[-1]
