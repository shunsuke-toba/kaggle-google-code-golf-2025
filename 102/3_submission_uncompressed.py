R=range(12);s=sum
def p(g):
 for x in R:
  for y in R:
   for l in R:
    m=g[y:y+l+2];i=m[1:-1]
    if 20*-~l-s(s(r[x:x+l+2])for r in m)<1>s(s(r[x+1:x+l+1])for r in i):
     for r in i:r[x+1:x+l+1]=[2]*l
 return g