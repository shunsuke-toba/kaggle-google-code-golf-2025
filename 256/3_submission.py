def p(j,R=range):
 for r in R(len(j)):
  if j[r][0]:break
 for y in R(len(j)):
  for x in R(sum(j[r])//2+r-y):j[y][x]=2+(y<r)-(y>r)
 return j
