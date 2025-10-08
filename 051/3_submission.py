p=lambda g:exec("""g[:]=map(list,zip(*g[::-1]))
for r in g:
 i=u=t=0
 for a in r:t|=u*a|-(u==a>0);u=u or a;r[i]=a or(t>0)*u;i+=1
"""*4)or g