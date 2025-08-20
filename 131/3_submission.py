t=lambda a:[*map(list,zip(*a))]
def p(a):
 h=len(a);w=len(a[0])
 if w>h:return t(p(t(a)))
 r=0;g=h
 for i,R in enumerate(a):
  if R[0]==2:r=i
  if 3 in R:g=min(g,i);G=i
 if g<r:return p(a[::-1])[::-1]
 return a[:r+1]+a[g:G+1]+[[8]*w]+[[0]*w]*(h-r+g-G-3)
