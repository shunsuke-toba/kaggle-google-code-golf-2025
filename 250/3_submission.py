def p(g):
 a=sum(g,[]);r,c=divmod(a.index(2)-11,10);o=[[0]*10for _ in g];k=-1
 for v in a:k+=1;o[min(max(k//10,r),r+3)][min(max(k%10,c),c+3)]|=v
 return o