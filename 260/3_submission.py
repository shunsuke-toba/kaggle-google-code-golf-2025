def p(g,a=9,b=-9):
 for n in range(100):
  v=g[i:=n//10][j:=n%10]
  if v==5:a=min(a,j-i);b=max(b,j-i)
  elif v:c=v;d=j-i
 g=[d]+[b+2]*(b>d)+[a-2]*(a<d)
 return [[c*(j-i in g)for j in range(10)]for i in range(10)]
