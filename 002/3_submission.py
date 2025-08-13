def p(j):
 A=range;c=len(j);R=A(c)
 for r in j:r[:]=[x or 4 for x in r]
 for _ in A(c+c):
  for r in R:
   for q in R:
    if j[r][q]==4 and( r<1 or q<1 or r+1==c or q+1==c or j[r-1][q]==0 or j[r+1][q]==0 or j[r][q-1]==0 or j[r][q+1]==0):j[r][q]=0
 return j
