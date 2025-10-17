def p(o):
 n=len(o);(a,r),(c,d)=[(e,q)for e in range(n)for q in range(n)if o[e][q]&1]
 def f(a,r,c,d,t,u=0):
  if n>(e:=a+c)>-1<(q:=r+d)<n:
   if o[e][q]==2:return o[e][q]
   if o[e][q]^8 and f(e,q,c,d,t,1):o[e][q]=3;return o[e][q]
   if u and o[e][q]*t>7:return f(a,r,d,-c,t-1,u)or f(a,r,-d,c,t-1,u)
 f(a,r,a-c,r-d,2)or f(c,d,c-a,d-r,2)
 return o