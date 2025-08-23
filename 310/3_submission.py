p=lambda m:(s:=sum(m,[]),c:=min(s,key=s.count),n:=s.count(c)//4+1,d:=divmod(s.index(c),len(m)))and[r[d[1]:d[1]+n]for r in m[d[0]:d[0]+n]]

