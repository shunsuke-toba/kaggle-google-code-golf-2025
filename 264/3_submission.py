def p(g):
 r=range;a=r(9);d=4,7,8,13,0,19,16,25,20;o=[[5]*9 for _ in a]
 for y in r(len(g)-2):
  for x in r(len(g[0])-2):
   if all(t:=[g[y+i//3][x+i%3]for i in a]):
    for i in a:o[(k:=d.index(sum(i*(t[i]!=5)for i in a)))-k%3+i//3][k%3*3+i%3]=t[i]
 return o
