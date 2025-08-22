def p(g):
 a=[];b=[];t=a
 for y,r in enumerate(g):
  if 4 in r:t+=[[y,r.index(4),10+~r[::-1].index(4)]]
  elif t:t=b
 if len(a)*(a[0][2]+~a[0][1])>len(b)*(b[0][2]+~b[0][1]):a,b=b,a
 for t,c in(a,1),(b,2):
  y0,y1,x0,x1=t[0][0],t[-1][0],t[0][1],t[0][2]
  for y in range(-~y0,y1):g[y][-~x0:x1]=[c]*(~x0+x1)
 return g
