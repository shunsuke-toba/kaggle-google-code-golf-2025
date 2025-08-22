def p(g):
 r=range;a=r(9);d=11,23,38,89,0,308,200,464,416;o=[[5]*9for _ in a]
 for y in r(len(g)-2):
  for x in r(len(g[0])-2):
   if all(t:=[g[y+i//3][x+i%3]for i in a]):
    k=d.index(sum((t[i]!=5)<<i for i in a))
    for i in a:o[k//3*3+i//3][k*3%9+i%3]=t[i]
 return o
