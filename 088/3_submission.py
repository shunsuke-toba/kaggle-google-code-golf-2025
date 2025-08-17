from collections import*
def p(a):
 c=Counter(sum(a,[]));k=[v for v in c if c[v]==4][0];y,x=zip(*[(i,j)for i,r in enumerate(a)for j,v in enumerate(r)if v==k]);return[[v and k for v in r[min(x)+1:max(x)]]for r in a[min(y)+1:max(y)]]
