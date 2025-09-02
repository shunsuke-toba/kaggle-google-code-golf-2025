def p(g):
 w=len(g[0])+1;f=sum((r+[0]for r in g),[])+[0]*w
 for i in(g:=[f.index(2)]):
  if f[i]:f[i]=0;g+=i+1,i-1,i+w,i-w
 return[8-8*(2in f)],