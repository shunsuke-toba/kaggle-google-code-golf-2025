def p(g):
 a=range(9);o=[[5]*9for _ in a]
 for x in range(1300):
  if all(t:=[g[x%97%(len(g)-2)+i//3][x%(len(g[0])-2)+i%3]for i in a]):
   for i in a:o[(k:='ehinatqzu'.find(chr(97+sum(i*(t[i]!=5)for i in a))))-k%3+i//3][k%3*3+i%3]=t[i]
 return o