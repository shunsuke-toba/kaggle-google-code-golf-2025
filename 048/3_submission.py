def p(g,o=0):
 w=len(g[0])+2
 f=[0]*w
 for r in g:f+=0,*r,0
 f+=f[:w]
 s=[f.index(2)]
 for i in s:
  if(v:=f[i]):f[i]=0;s+=i+1,i-1,i+w,i-w;o+=v<3
 return[[o&8]]
