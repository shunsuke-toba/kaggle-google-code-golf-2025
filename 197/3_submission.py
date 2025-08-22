p=lambda g:(t:=next(filter(all,g)))and[[{a:b for a,b in zip(t,r)if b}.get(c,0)for c in t]for r in g]
