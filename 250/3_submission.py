def p(g):
 a=sum(g,[]);r,c=divmod(a.index(2)-11,10);i=j=0;I=r
 for v in a:g[i][j]-=v;g[I][min(max(j,c),c+3)]|=v;i+=j>8;j=-~j%10;I+=i>I<r+3
 return g