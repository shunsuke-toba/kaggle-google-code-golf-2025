def p(a):y,x=map(min,zip(*(divmod(i,10)for i,v in enumerate(sum(a,[]))if v)));return[r[x:x+3]for r in a[y:y+3]]
