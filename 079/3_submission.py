p=lambda g,r=range(12):max(a:=[t for i in r for j in r if all(map(sum,(t:=[x[j:j+3]for x in g[i:i+3]])+[*zip(*t)]))],key=a.count)
