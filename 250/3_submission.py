def p(g):
 a=sum(g,[]);r,c=divmod(a.index(2)-11,10);k=0
 for v in a:g[k//10][k%10]-=v;g[min(max(k//10,r),r+3)][min(max(k%10,c),c+3)]|=v;k+=1
 return g