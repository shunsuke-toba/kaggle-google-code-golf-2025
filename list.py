import os
len_sum = 0
rest = 0
for i in range(1, 401):
    src = f"{i:03}/3_submission.py"
    if os.path.exists(src):
        # 中身が書かれているか
        with open(src, 'rb') as f:
            content = f.read()
        if len(content) <= 1:
            print(f"{i:03d} : unsolved")
            rest += 1
        else:
            print(f"{i:03d} : {len(content)}")
            len_sum += 2500 - len(content)
print(f"Score : {len_sum}")
print(f"Rest : {rest}")