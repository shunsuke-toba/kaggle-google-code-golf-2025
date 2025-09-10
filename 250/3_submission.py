def p(g):
 a=sum(g,[]);r,c=divmod(a.index(2)-11,m:=10);k=0
 for v in a:g[k//m][k%m]-=v;g[min(max(k//m,r),r+3)][min(max(k%m,c),c+3)]|=v;k+=1
 return g