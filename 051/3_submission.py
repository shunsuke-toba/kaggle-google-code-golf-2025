p=lambda g:exec("""g[:]=map(list,zip(*g[::-1]))
for r in g:
 y=-1
 for b in r[1:]:
  if 2>sum(g,[]).count(a:=r[y:=y+1])>b:r[:y]=map({0:a}.get,r[:y],r)
"""*4)or g