def p(g):
 b=sum(g,[]);I=b.index;g=[[0]*10for _ in g];j=0
 for v in b:g[(j+I(1)-I(v or 1))//10][j%10]+=v;j+=1
 return g