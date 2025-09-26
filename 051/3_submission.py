p=lambda g:exec("""g[:]=map(list,zip(*g[::-1]))
for r in g:
 i=u=t=0
 for a in r:
  if u==a>0:break
  u=u or a;t|=u!=a>0;r[i]=a or u*t;i+=1
"""*4)or g