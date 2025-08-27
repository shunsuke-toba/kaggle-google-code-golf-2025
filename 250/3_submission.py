def p(g):
 a=sum(g,[]);r,c=divmod(a.index(2)-11,10);o=[[0]*10for _ in g]
 for k in range(100):o[min(max(k//10,r),r+3)][min(max(k%10,c),c+3)]|=a[k]
 return o
