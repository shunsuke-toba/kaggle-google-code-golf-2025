def p(g):
    si = [99] * 10
    sj = [99] * 10
    ti = [0] * 10
    tj = [0] * 10
    cnt = [0] * 10
    h = len(g)
    w = len(g[0])

    for i in range(h):
        for j in range(w):
            c = g[i][j]
            cnt[c] += 1
            si[c] = min(si[c], i)
            ti[c] = max(ti[c], i)
            sj[c] = min(sj[c], j)
            tj[c] = max(tj[c], j)

    baseColor = 0
    for i in range(1, 10):
        if cnt[baseColor] < cnt[i]:
            baseColor = i

    for c in range(1, 10):
        if c == baseColor:
            continue
        subH = ti[c] - si[c] + 1
        subW = tj[c] - sj[c] + 1
        if subH <= 0:
            continue
        bx, by = 1, 1
        for padH in range(-(subH % 2), 1):
            for padW in range(-(subW % 2), 1):
                ok = True
                for i in range((subH + 1) // 2):
                    for j in range((subW + 1) // 2):
                        x = si[c] + i * 2 + padH
                        y = sj[c] + j * 2 + padW
                        p_cnt = 0
                        s_cnt = 0
                        if x < 0 or y < 0:
                            s_cnt += 1
                        elif g[x][y] == c:
                            p_cnt += 1
                        if x + 1 >= h or y < 0:
                            s_cnt += 1
                        elif g[x + 1][y] == c:
                            p_cnt += 1
                        if x < 0 or y + 1 >= w:
                            s_cnt += 1
                        elif g[x][y + 1] == c:
                            p_cnt += 1
                        if x + 1 >= h or y + 1 >= w:
                            s_cnt += 1
                        elif g[x + 1][y + 1] == c:
                            p_cnt += 1
                        if p_cnt != 0 and p_cnt + s_cnt != 4:
                            ok = False
                if ok:
                    bx = padH
                    by = padW
                    break
            if bx != 1:
                break
        if bx == 1:
            continue
        bx -= si[c] % 2
        by -= sj[c] % 2
        t = [[0] * ((w-by + 1) // 2) for _ in range((h-bx + 1) // 2)]
        for i in range((h-bx + 1) // 2):
            for j in range((w-by + 1) // 2):
                x = i * 2 + bx
                y = j * 2 + by
                p_cnt = 0
                s_cnt = 0
                if x < 0 or y < 0:
                    s_cnt += 1
                elif g[x][y] == c:
                    p_cnt += 1
                if x + 1 >= h or y < 0:
                    s_cnt += 1
                elif g[x + 1][y] == c:
                    p_cnt += 1
                if x < 0 or y + 1 >= w:
                    s_cnt += 1
                elif g[x][y + 1] == c:
                    p_cnt += 1
                if x + 1 >= h or y + 1 >= w:
                    s_cnt += 1
                elif g[x + 1][y + 1] == c:
                    p_cnt += 1
                t[i][j] = 1 if p_cnt > 0 else 0

        for tar in range(1, 10):
            if tar == c or tar == baseColor:
                continue
            subH_tar = ti[tar] - si[tar] + 1
            subW_tar = tj[tar] - sj[tar] + 1
            if subH_tar <= 0:
                continue
            for bx2 in range(-h, h):
                for by2 in range(-w, w):
                    ok = True
                    for i in range(len(t)):
                        for j in range(len(t[0])):
                            if bx2 + i < 0 or by2 + j < 0 or bx2 + i >= h or by2 + j >= w:
                                if t[i][j] == 1:
                                    ok = False
                                    break
                                else:
                                    continue
                            if t[i][j] == 1 and g[bx2 + i][by2 + j] != tar:
                                ok = False
                                break
                            if t[i][j] == 0 and g[bx2 + i][by2 + j] == tar:
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        ans = [[0] * subW_tar for _ in range(subH_tar)]
                        for i in range(si[tar], ti[tar] + 1):
                            for j in range(sj[tar], tj[tar] + 1):
                                ans[i - si[tar]][j - sj[tar]] = baseColor if g[i][j]!=tar else tar
                        return ans