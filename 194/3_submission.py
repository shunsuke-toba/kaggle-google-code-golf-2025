p=lambda g:[*map(list.extend,g,zip(*g[::-1]))]and g+[r[::-1]for r in g[::-1]]
