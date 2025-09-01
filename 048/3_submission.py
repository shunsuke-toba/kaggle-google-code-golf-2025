def p(g):
 f=[]
 for r in g:f+=*r,0
 w=len(g[0])+1;f+=w*[0]
 for i in(g:=[f.index(2)]):
  if f[i]:f[i]=0;g+=i+1,i-1,i+w,i-w
 return[8-8*(2in f)],