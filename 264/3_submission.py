def p(g):
 a=range(9);w=len(g[0])-2;d={}
 for x in range((len(g)-2)*w):
  if all(t:=[g[x//w+i//3][x%w+i%3]for i in a]):d['ehinatqzu'.find(chr(97+sum(i*(t[i]!=5)for i in a)))]=t
 return[[d[r-r%3+c//3][r%3*3+c%3]for c in a]for r in a]