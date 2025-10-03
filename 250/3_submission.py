def p(g):
 a=sum(g,[]);r,d=divmod(a.index(2)-8,10);i=j=0;I=r
 for v in a:g[i][j]-=v;g[I][min(max(j,d-3),d)]|=v;i+=j>8;j=-~j%10;I+=i>I<r+3
 return g