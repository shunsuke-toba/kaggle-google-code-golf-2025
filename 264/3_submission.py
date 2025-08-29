def p(g):
 a=range(9);w=len(g[0])-2;o=[[5]*9for _ in a]
 for x in range((len(g)-2)*w):
  if all(t:=[g[x//w+i//3][x%w+i%3]for i in a]):
   for i in a:o[(k:='ehinatqzu'.find(chr(97+sum(i*(t[i]!=5)for i in a))))-k%3+i//3][k%3*3+i%3]=t[i]
 return o