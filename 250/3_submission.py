def p(g):
 a=sum(g,[]);k=a.index(2)-8;I=r=k//10;i=j=0
 for v in a:g[i][j]-=v;g[I][min(max(j,k%10-3),k%10)]|=v;i+=j>8;j=-~j%10;I+=i>I<r+3
 return g