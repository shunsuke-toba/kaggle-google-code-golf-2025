def p(g):
 h=len(g);w=len(g[0])
 f=lambda x,y:h>x>-1<y<w and g[x][y]and(g[x].__setitem__(y,0),f(x+1,y),f(x-1,y),f(x,y+1),f(x,y-1))and 1
 n=sum(f(*divmod(t,w))for t in range(h*w))
 return[[0]*i+[8]+[0]*(n+~i)for i in range(n)]
