def p(g):r=range(12);a=[t for i in r for j in r if all(map(sum,(t:=[x[j:j+3]for x in g[i:i+3]])+[*zip(*t)]))];return max(a,key=a.count)
