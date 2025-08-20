def p(j):
 l,J=len(j),len(j[0])
 def f(a,b,e):
  if l>a>-1<b<J and j[a][b]<1:j[a][b]=e;[f(a+d,b,e)or f(a,b+d,e)for d in(-1,1)]
 f(0,0,1);[f(l//2-1+(i&1),J//2-1+i//2,2)for i in range(4)];f(l-1,J-1,3);return j
