def p(g):
 f=[divmod(i,len(g[0]))for i,v in enumerate(sum(g,[]))if v==4];(a,b),(c,d)=f[0],f[-1];L,R=g[a+1][b],g[a+1][d];h=c-a-1;w=d-b-1
 i,j=map(min,zip(*[(i,j)for i,r in enumerate(g)for j,u in enumerate(r)if u and u-4 and not(a<=i<=c and j in(b,d))]));S=i
 while g[i][j]<1:i+=1
 f=g[i][j]==R
 o=[[0]*(w+2)for _ in range(h+2)]
 o[0][0]=o[0][-1]=o[-1][0]=o[-1][-1]=4
 for i in range(h):
  o[i+1][0]=L;o[i+1][-1]=R;r=g[S+i][j:j+w];o[i+1][1:-1]=r[::-1]if f else r
 return o
