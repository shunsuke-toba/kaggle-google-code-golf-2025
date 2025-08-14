def p(g):
 h,w=len(g),len(g[0]);A=[i for i,r in enumerate(g)if r[0]==2];B=[i for i,r in enumerate(g)if r[-1]==2];e=any(8 in g[i]for i in A);d=2*e-1;S,T=((B,A),(A,B))[e];c=(w-1)*(not e);[8 in(R:=g[r])and[j:=R.index(8),[R.__setitem__(k,8)for k in range(c+d,j,d)],R.__setitem__(j,4),u:=T[0]+r-S[0],0<=u<h and[g[u].__setitem__(k,8)for k in range(w-1-c-d,e and-1 or w,-d)]]for r in S];return g
