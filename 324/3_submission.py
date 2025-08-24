def p(g,R=range):
 f=sum(g,[]);a=max(g[0][:2]+g[1][:2],key=f.count);b=max({*f}-{a},key=f.count)
 s=[];m=[0]*10
 for i,r in enumerate(g):
  for j,d in enumerate(r):
   if d in(a,b):continue
   s+=i+j,60+i-j,
   m[a if a in r and a in[t[j]for t in g]else b]=d
 return [[(d,m[d])[d in(a,b)and(i+j in s or 60+i-j in s)]for j,d in enumerate(g[i])]for i in R(len(g))]
