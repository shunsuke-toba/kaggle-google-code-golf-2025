def p(r):
 n=min(a for a,r in enumerate(r)for f,u in enumerate(r)if u==8)
 m=min(f for a,r in enumerate(r)for f,u in enumerate(r)if u==8)
 u=[(e:=a-n,f-m)for a,r in enumerate(r)for f,u in enumerate(r)if u==8]
 n=min(a for a,r in enumerate(r)for f,u in enumerate(r)if u%8)
 m=min(f for a,r in enumerate(r)for f,u in enumerate(r)if u%8)
 r=[r[m:m+e+3]for r in r[n:n+e+3]]
 for a,f in u:r[a+1][f+1]=(a-f)*(a+f-e)and(r[-1][1],r[1][0],r[1][-1],r[0][1])[(a<f)*2+(a+f<e)]or 8
 return r