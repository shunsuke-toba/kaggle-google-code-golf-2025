def p(grid):
    # Component-based pattern copy per 1_solution.md
    H, W = len(grid), len(grid[0])

    def inb(r, c):
        return 0 <= r < H and 0 <= c < W

    # Build connected components of non-zero cells
    vis = [[0] * W for _ in range(H)]
    comps = []
    for r in range(H):
        for c in range(W):
            if grid[r][c] == 0 or vis[r][c]:
                continue
            q = [(r, c)]
            vis[r][c] = 1
            qi = 0
            cells = []
            counts = {}
            by_color = {}
            while qi < len(q):
                rr, cc = q[qi]
                qi += 1
                v = grid[rr][cc]
                cells.append((rr, cc, v))
                counts[v] = counts.get(v, 0) + 1
                if v not in by_color:
                    by_color[v] = []
                by_color[v].append((rr, cc))
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = rr + dr, cc + dc
                    if inb(nr, nc) and not vis[nr][nc] and grid[nr][nc] != 0:
                        vis[nr][nc] = 1
                        q.append((nr, nc))
            comps.append({'cells': cells, 'counts': counts, 'by_color': by_color})

    # Detect source components: >=4 colors and exactly 3 singleton colors
    sources = []
    for comp in comps:
        cols = list(comp['counts'].keys())
        if len(cols) < 4:
            continue
        singles = [col for col, n in comp['counts'].items() if n == 1]
        if len(singles) != 3:
            continue
        # wire = most frequent color
        wire = None
        best = -1
        for col, n in comp['counts'].items():
            if n > best:
                wire = col
                best = n
        anchors = {}
        for col in singles:
            anchors[col] = comp['by_color'][col][0]
        wires = [(r, c) for (r, c, v) in comp['cells'] if v == wire]
        sources.append({'wire': wire, 'anchors': anchors, 'wires': wires, 'cells': comp['cells']})

    out = [row[:] for row in grid]
    if not sources:
        return out

    # 8 dihedral transforms on vectors
    def transforms(v):
        x, y = v
        return [
            ( x,  y),
            (-y,  x),
            (-x, -y),
            ( y, -x),
            ( x, -y),
            ( y,  x),
            (-x,  y),
            (-y, -x),
        ]

    # Remove source cells from output
    src_cells = set()
    for s in sources:
        for (r, c, v) in s['cells']:
            src_cells.add((r, c))
            out[r][c] = 0

    # Replicate each source pattern on all matching anchor triples elsewhere
    for s in sources:
        wire = s['wire']
        labels = list(s['anchors'].keys())
        A, B, C = labels[0], labels[1], labels[2]
        ar, ac = s['anchors'][A]
        br, bc = s['anchors'][B]
        cr, cc = s['anchors'][C]

        # candidate target positions per label (outside sources)
        posA, posB, posC = [], [], []
        for r in range(H):
            for c in range(W):
                if (r, c) in src_cells:
                    continue
                v = grid[r][c]
                if v == A:
                    posA.append((r, c))
                elif v == B:
                    posB.append((r, c))
                elif v == C:
                    posC.append((r, c))

        # source vectors (relative to A)
        vab = (br - ar, bc - ac)
        vac = (cr - ar, cc - ac)

        used = set()
        for ta in posA:
            for tb in posB:
                for tc in posC:
                    if ta == tb or ta == tc or tb == tc:
                        continue
                    dab = (tb[0] - ta[0], tb[1] - ta[1])
                    dac = (tc[0] - ta[0], tc[1] - ta[1])
                    t_vab = transforms(vab)
                    t_vac = transforms(vac)
                    k = -1
                    for i in range(8):
                        if t_vab[i] == dab and t_vac[i] == dac:
                            k = i
                            break
                    if k < 0:
                        continue
                    if (ta, tb, tc) in used:
                        continue
                    used.add((ta, tb, tc))
                    def apply(vec):
                        return transforms(vec)[k]
                    for (wr, wc) in s['wires']:
                        vr, vc = wr - ar, wc - ac
                        dr, dc = apply((vr, vc))
                        tr, tc2 = ta[0] + dr, ta[1] + dc
                        if inb(tr, tc2):
                            if (tr, tc2) == ta or (tr, tc2) == tb or (tr, tc2) == tc:
                                continue
                            if out[tr][tc2] == 0:
                                out[tr][tc2] = wire

    return out
