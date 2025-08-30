def p(g,b=0):
 for n in range(400):
  y=n//20;r=0;a=[]
  while y<20>(s:=g[y][n%20:]+[0])[0]>0:x=s.index(0);r+=sum(t:=s[:x])-x;a+=t,;y+=1
  if r>b:o,b=a,r
 return o