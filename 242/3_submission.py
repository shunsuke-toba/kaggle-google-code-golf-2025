def p(g):s=sum(g,[]).index(0);return[r[~s&15::-1][:3]for r in g[s//16:][:3]]
