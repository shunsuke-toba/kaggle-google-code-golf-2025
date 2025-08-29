def p(g):
 b=sum(g,[]);I=b.index;g=[[0]*10for _ in g]
 for j,v in enumerate(b):g[(j+I(1)-I(v or 1))//10][j%10]+=v
 return g