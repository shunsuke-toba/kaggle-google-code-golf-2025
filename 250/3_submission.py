def p(g):
 a=sum(g,[]);r,c=divmod(a.index(2),10);o=[[0]*10for _ in g]
 for k in range(100):o[min(max(k//10,r-1),r+2)][min(max(k%10,c-1),c+2)]|=a[k]
 return o
