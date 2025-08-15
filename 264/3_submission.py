def p(g):
 r=range
 d={0:4,11:0,38:2,23:1,89:3,308:5,464:7,200:6,416:8}
 o=[[5]*9 for _ in r(9)]
 for y in r(len(g)-2):
  for x in r(len(g[0])-2):
   t=[g[y+a][x+b]for a in r(3)for b in r(3)]
   if 0 in t:continue
   k=d[sum(1<<i for i in r(9)if t[i]-5)]
   for i in r(9):o[k//3*3+i//3][k%3*3+i%3]=t[i]
 return o
