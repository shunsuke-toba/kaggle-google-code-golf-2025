def p(g):
 r=range;a=r(9);o=[[5]*9for _ in a]
 for y in r(len(g)-2):
  for x in r(len(g[0])-2):
   if all(t:=[g[y+i//3][x+i%3]for i in a]):
    for i in a:o[(k:='ehinatqzu'.find(chr(97+sum(i*(t[i]!=5)for i in a))))-k%3+i//3][k%3*3+i%3]=t[i]
 return o