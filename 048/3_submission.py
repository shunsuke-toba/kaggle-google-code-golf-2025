def p(g):
 w=len(g[0])+2;f=[0]*w
 for r in g:f+=0,*r,0
 f+=f[:w];s=[f.index(2)]
 for i in s:
  if f[i]:f[i]=0;s+=i+1,i-1,i+w,i-w
 return[8-8*(2in f)],