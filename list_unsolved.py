import os, shutil
for i in range(1, 401):
    src = f"{i:03}/3_submission.py"
    if os.path.exists(src):
        # 中身が書かれているか
        with open(src, 'r') as f:
            content = f.read()
        if len(content) < 10:
            print(f"File {src} is not written.")