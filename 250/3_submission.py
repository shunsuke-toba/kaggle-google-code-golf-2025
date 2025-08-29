def p(g):
 a=sum(g,[]);r,c=divmod(a.index(2)-11,10);g=[[0]*10for _ in g];k=0
 for v in a:g[min(max(k//10,r),r+3)][min(max(k%10,c),c+3)]|=v;k+=1
 return g