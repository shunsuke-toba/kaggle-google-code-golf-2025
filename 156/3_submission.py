def p(g):
 a=[];b=[];t=a
 for y,r in enumerate(g):
  if 4 in r:t+=[[y,r.index(4),9-r[::-1].index(4)]]
  elif t:t=b
 if len(a)*(a[0][2]+~a[0][1])>len(b)*(b[0][2]+~b[0][1]):a,b=b,a
 for t,c in(a,1),(b,2):
  for y in range(-~t[0][0],t[-1][0]):g[y][-~t[0][1]:t[0][2]]=[c]*(t[0][2]+~t[0][1])
 return g
