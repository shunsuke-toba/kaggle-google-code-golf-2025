p=lambda g:(f:=sum(g,[]),c:=max({*f}-{0},key=f.count),[[c*(v==c or v*(v-c)and(c in[R[j]for R in g[i-1:i]+g[i+1:i+2]] and c in r[j-1:j]+r[j+1:j+2]))for j,v in enumerate(r)]for i,r in enumerate(g)])[2]
