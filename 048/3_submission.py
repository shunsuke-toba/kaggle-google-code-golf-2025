def p(g):
 w=len(g[0])+2;f=[0]*w*2
 for r in g:f[w:w]=0,*r,0
 for i in(s:=[f.index(2)]):
  if f[i]:f[i]=0;s+=i+1,i-1,i+w,i-w
 return[8-8*(2in f)],