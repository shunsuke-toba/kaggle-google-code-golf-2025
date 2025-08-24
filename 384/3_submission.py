def p(g):g=[r for r in g if any(r)];g=list(zip(*g));g=[c for c in g if any(c)];return[sum(zip(r,r),())for r in zip(*g) for _ in"00"]
