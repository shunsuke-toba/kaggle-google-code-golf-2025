p=lambda g:(h:=[[r[o:o+2]for r in g[p:p+2]]for p in(0,3)for o in(0,3)])and min(h,key=h.count)
