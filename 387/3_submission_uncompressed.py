def p(n):
 (a,u,r),(a,d,t),(f,u,s),(f,d,s)=e=[(p,u,d)for p,u in enumerate(n)for u,d in enumerate(u)if d]
 for p in range(u,d+1):n[a][p]=n[f][p]=5-min(p-u,d-p)%2*5
 for p in range(a,f+1):n[p][u]=n[p][d]=5-min(p-a,f-p)%2*5
 for p,u,d in e:n[p][u-1:u+2]=n[p-1][u-1:u+2]=n[p+1][u-1:u+2]=[r^t^d]*3;n[p][u]=d
 return n